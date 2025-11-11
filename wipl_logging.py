from datetime import datetime
import pandas as pd
import numpy as np
import os
from params_dicts import PARAMS_DICTS

log_file = None #placeholder logfile handle so global log file handle is defined

def print_and_log(message):
    """Print to console and write to log file"""
    print(message)
    if log_file:
        log_file.write(str(message) + '\n')
        log_file.flush()  # Ensure it's written immediately

def update_logging_sheet(mm, ms, p, ri, time_taken, SAVE_DIR):

    LOG_PATH = r"G:\My Drive\WIPL\WIPL results\scatterer_database_log.csv"

    params = PARAMS_DICTS[p]

    frequencies = params['frequencies'] #GHz
    lengths = params['lengths'] #mm
    slants = params['slants']
    pitches = params['pitches']

    n_combs = np.prod([len(x) for x in [frequencies, lengths, slants, pitches]])

    new_df_row = pd.DataFrame({
        'date' : [datetime.now().strftime("%d/%m/%Y")],
        'model_main' : [mm],
        'model_suffix' : [ms],
        'run_id' : [ri],
        'params_dict' : [p],
        'time_taken' : [np.round(time_taken,0)],
        'frequencies' : [frequencies],
        'pitches' : [pitches],
        'lengths' : [lengths],
        'slants' : [slants],
        'n_combs' : [n_combs*2], #for polarisation
        'results_path' : [os.path.join(SAVE_DIR, f'{ri}.nc')],
    }, index=None)

    log_df = pd.read_csv(LOG_PATH)

    updated_log = pd.concat([log_df, new_df_row], ignore_index =True)

    updated_log.to_csv(LOG_PATH, index = False)

    