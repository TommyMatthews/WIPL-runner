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

WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

DATASET_GENERATED = False

# PATH TO FOLDER FULL OF WIPL MODEL MAIN FOLDERS
BASE_PATH = r"G:\My Drive\WIPL\WIPL models"   

RESULTS_BASE_PATH = r"G:\My Drive\WIPL\WIPL results"

# set up to always run a horizontal and vertical run
pol_run_dict = {
    "H" : [1,0],
    "V" : [0,1]
}

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

def save_file(ds, model_main, model_suffix, run_id):
    
    MODEL_MAIN_DIR = os.path.join(RESULTS_BASE_PATH, f'{model_main}')
    MODEL_SPECIFIC_DIR = os.path.join(MODEL_MAIN_DIR, f'{model_suffix}') 
    RESULTS_SAVE_PATH = os.path.join(MODEL_SPECIFIC_DIR, f'{run_id}.nc') #CHANGE BACK TO .NC!!!!

    if not os.path.isdir(MODEL_MAIN_DIR):
        os.mkdir(MODEL_MAIN_DIR)

    if not os.path.isdir(MODEL_SPECIFIC_DIR):
        os.mkdir(MODEL_SPECIFIC_DIR)

    ds.to_netcdf(RESULTS_SAVE_PATH)


def print_live_time(start):
    pass

if __name__ == "__main__":

    start = time.time()

    mm, ms, p, ri = get_arguments()

    PROJECT_PATH = BASE_PATH + f'\\{mm}\\{mm}_{ms}'

    SYMB_PATH = PROJECT_PATH + '.SMB'

    if not os.path.isfile(SYMB_PATH):
        print('Specified file does not exist, check input args.')

    SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)
    
    pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

    params = PARAMS_DICTS[p]

    frequencies = params['frequencies'] #GHz
    lengths = params['lengths'] #mm
    slants = params['slants']
    pitches = params['pitches']

    
    counter = 1
    ds = None

    for frequency in frequencies:
        for length in lengths:
            for slant in slants:
                for pitch in pitches:
                    for pol in pol_run_dict:
                        
                        SymbolsList.SetSymbolByName("f", frequency)
                        SymbolsList.SetSymbolByName("Re_body", PERMITTIVITY_DICT["bug"][frequency]["Re_body"])
                        SymbolsList.SetSymbolByName("Im_body", PERMITTIVITY_DICT["bug"][frequency]["Im_body"])
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

                        print(kwargs)

                        SymbolsList.PrintSymbols()

                        #SymbolsList.PrintSymbols()

                        pro.Run(PROJECT_PATH)

                        far_field = wiplpy.WResults.InitializeFFResults(PROJECT_PATH)

                        if far_field: 

                            print('RESULTS PRESENT')
                        
                            theta = far_field.GetThetaPoints()[0]
                            frequency = far_field.GetFrequencies()[0]

                            results_extractor = FFObjToDictConverter(far_field, theta, frequency)

                            results_dict = results_extractor.get_output_dict()

                            if not DATASET_GENERATED:
                                ds = create_placeholder_dataset(results_dict, frequencies, lengths, slants, pitches)
                                DATASET_GENERATED = True

                            ds = input_single_sim_results(ds, pol, results_dict, kwargs)

                        else: 

                            print('NO RESULTS')                    

                        end = time.time()
                        print(f'Combination {counter} done, {end-start:.4f} s total elapsed')
                        counter +=1

    if ds:
        ds = add_metadata(ds)
        save_file(ds, mm, ms, ri) #CHANGE BACK TO DS

    else:
        print('NO RESULTS GENERATED: nothing saved... :/')

    end = time.time()
    print(f'Saved {ri}')
    print(f'Time taken: {end-start:.4f} s')

                    