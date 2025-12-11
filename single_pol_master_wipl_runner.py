import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter
import time
import csv
import io
import os
import sys
import argparse 

# import pandas as pd

import pickle

from params_dicts import PARAMS_DICTS, PERMITTIVITY_DICT
from netcdf_manager import create_placeholder_dataset, input_single_sim_results, add_metadata
from wipl_logging import update_logging_sheet 

WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

DATASET_GENERATED = False

# PATH TO FOLDER FULL OF WIPL MODEL MAIN FOLDERS
BASE_PATH = r"G:\My Drive\WIPL\WIPL models"   

RESULTS_BASE_PATH = r"G:\My Drive\WIPL\WIPL results"

# set up to always run a horizontal and vertical run
pol_run_dict = {
    "H" : [1,0],
    #"V" : [0,1]
}

# Global log file handle
log_file = None

def print_and_log(message):
    """Print to console and write to log file"""
    print(message)
    if log_file:
        log_file.write(str(message) + '\n')
        log_file.flush()  # Ensure it's written immediately

def get_arguments():
    """
    Retrieve four arguments from user input:
    - model_main (mm): Main model name
    - model_suffix (ms): Model suffix
    - params_dict (pd): Name of the parameters dictionary
    - run_id (ri): Run identifier
    """
    parser = argparse.ArgumentParser(description='Retrieve model arguments')
    
    parser.add_argument('--mm', '--model_main', 
                       dest='model_main',
                       type=str, 
                       required=True,
                       help='Main model name')
    
    parser.add_argument('--ms', '--model_suffix',
                       dest='model_suffix',
                       type=str,
                       required=True,
                       help='Model suffix')
    
    parser.add_argument('--p', '--params_dict',
                       dest='params_dict',
                       type=str,
                       required=True,
                       help='Params dict name')
    
    parser.add_argument('--ri', '--run_id',
                       dest='run_id',
                       type=str,
                       required=True,
                       help='Run identifier')
    
    args = parser.parse_args()

    
    return args.model_main, args.model_suffix, args.params_dict, args.run_id

def save_file(ds, save_dir, run_id):
    
    RESULTS_SAVE_PATH = os.path.join(save_dir, f'{run_id}.nc') #CHANGE BACK TO .NC!!!!

    ds.to_netcdf(RESULTS_SAVE_PATH)


if __name__ == "__main__":

    start = time.time()

    mm, ms, p, ri = get_arguments()

    PROJECT_PATH = BASE_PATH + f'\\{mm}\\{mm}_{ms}'

    SYMB_PATH = PROJECT_PATH + '.SMB'

    if not os.path.isfile(SYMB_PATH):
        print(SYMB_PATH)
        print('Specified file does not exist, check input args.')

    # Open log file
    SAVE_DIR = os.path.join(RESULTS_BASE_PATH, f'{mm}', f'{ms}')
    LOG_DIR = os.path.join(SAVE_DIR, 'log_files')
    if not os.path.isdir(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)
    LOG_PATH = os.path.join(LOG_DIR, f'{ri}_log.txt')
    log_file = open(LOG_PATH, 'w')

    SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)
    
    pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

    params = PARAMS_DICTS[p]

    frequencies = params['frequencies'] #GHz
    lengths = params['lengths'] #mm
    slants = params['slants']
    pitches = params['pitches']
    model_type = params['type']
    
    counter = 1
    ds = None

    for frequency in frequencies:
        for length in lengths:
            for slant in slants:
                for pitch in pitches:
                    for pol in pol_run_dict:
                        
                        SymbolsList.SetSymbolByName("f", frequency)
                        SymbolsList.SetSymbolByName("Re_body", PERMITTIVITY_DICT[model_type][frequency]["Re_body"])
                        SymbolsList.SetSymbolByName("Im_body", PERMITTIVITY_DICT[model_type][frequency]["Im_body"])

                        if Re_appendage := PERMITTIVITY_DICT[model_type][frequency].get("Re_appendage"):
                            SymbolsList.SetSymbolByName("Re_appendage", Re_appendage)
                        if Im_appendage := PERMITTIVITY_DICT[model_type][frequency].get("Im_appendage"):
                            SymbolsList.SetSymbolByName("Im_appendage", Im_appendage)
                        SymbolsList.SetSymbolByName("pitch", pitch)
                        SymbolsList.SetSymbolByName("slant", slant)
                        SymbolsList.SetSymbolByName("Ephi", pol_run_dict[pol][0])
                        SymbolsList.SetSymbolByName("Etheta", pol_run_dict[pol][1])
                        SymbolsList.SetSymbolByName("length_mm", length)

                        kwargs = {
                            'frequency' : frequency,
                            'length': length,
                            'pitch': pitch,
                            'slant': slant,     
                        }

                        print_and_log(kwargs)

                        #SymbolsList.PrintSymbols()

                        pro.Run(PROJECT_PATH)

                        far_field = wiplpy.WResults.InitializeFFResults(PROJECT_PATH)

                        if far_field: 

                            print_and_log('RESULTS PRESENT')
                        
                            theta = far_field.GetThetaPoints()[0]
                            frequency = far_field.GetFrequencies()[0]

                            results_extractor = FFObjToDictConverter(far_field, theta, frequency)

                            results_dict = results_extractor.get_output_dict()

                            if not DATASET_GENERATED:
                                ds = create_placeholder_dataset(results_dict, frequencies, lengths, slants, pitches)
                                DATASET_GENERATED = True

                            ds = input_single_sim_results(ds, pol, results_dict, kwargs)

                        else: 

                            print_and_log('NO RESULTS')                    

                        end = time.time()
                        print_and_log(f'Combination {counter} done, {end-start:.4f} s total elapsed')
                        counter +=1

                    if ds:
                        save_file(ds, SAVE_DIR, ri) #CHANGE BACK TO DS
                        print(f'Temp save {ri} for {frequency} GHz {length} mm {slant} deg {pitch} deg')


    end = time.time()

    time_taken = end-start  

    
    if ds:
        #ds = add_metadata(ds)
        save_file(ds, SAVE_DIR, ri) #CHANGE BACK TO DS
        print(f'Saved {ri}')

        update_logging_sheet(mm, ms, p, ri, time_taken, SAVE_DIR)

    else:
        print('NO RESULTS GENERATED: nothing saved... :/')
    
    
    print(f'Time taken: {time_taken:.4f} s')

                    