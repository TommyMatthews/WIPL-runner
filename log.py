import os
from params_dicts import PARAMS_DICTS, PERMITTIVITY_DICT
from master_wipl_runner import get_arguments, BASE_PATH, RESULTS_BASE_PATH, update_logging_sheet


if __name__ == "__main__":

    # Test file exists

    mm, ms, p, ri = get_arguments()

    PROJECT_PATH = BASE_PATH + f'\\{mm}\\{mm}_{ms}'

    time_taken = 0

    SAVE_DIR = os.path.join(RESULTS_BASE_PATH, f'{mm}', f'{ms}')

    update_logging_sheet(mm, ms, p, ri, time_taken, SAVE_DIR)

