import os
from params_dicts import PARAMS_DICTS, PERMITTIVITY_DICT
from master_wipl_runner import get_arguments, BASE_PATH


if __name__ == "__main__":

    # Test file exists

    mm, ms, p, ri = get_arguments()

    PROJECT_PATH = BASE_PATH + f'\\{mm}\\{mm}_{ms}'

    SYMB_PATH = PROJECT_PATH + '.SMB'

    if not os.path.isfile(SYMB_PATH):
        print(SYMB_PATH)
        print(f'PRE-CHECK FAILED FOR {ri}, PATH DOES NOT EXIST')

    # Test param exists

    try:
        params = PARAMS_DICTS[p]

        # Test permittivity exists

        if params['type'] not in ['bug', 'bird']:
            print(f'PRE CHECK FAILED FOR {ri}, INVALID SCATTERER TYPE')

        for f in params['frequencies']:

            try:
                scat_type = params['type']
                _ = PERMITTIVITY_DICT[scat_type][f]
            except KeyError:
                print(f'PRE CHECK FAILED FOR {ri}, MISSING PERMITTIVTY VALUES FOR TYPE/FREQUENCY COMBO {scat_type}/{f}')

    except KeyError:
        print(f'PRE CHECK FAILED FOR {ri}, PARAM DICT {p} DOES NOT EXIST')

    

