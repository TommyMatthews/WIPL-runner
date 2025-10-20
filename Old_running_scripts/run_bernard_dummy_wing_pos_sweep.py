import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter

import io
import os
import sys

# SET UP FOR PITCH AND SLANT ANALYSIS IN BOTH POLARISATIONS C-BAND

WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

# morpho_list = ['body_wing'] #['body_wing', 'body_leg', 'body']
# morpho_list = ['body_wing_leg']
wing_pos_list = ['mid', 'up', 'down'] # left out 'M' as already run

# frequency_name = '560'
# f = 5.6
# ReBody = 43
# ImBody = 19
# ReChitin = 5.1
# ImChitin = 0.12

frequency_name = '027'
f = 2.7
ReBody = 46
ImBody = 19
ReChitin = 5.3
ImChitin = 0.12


pol_run_dict = {
    "H" : [1,0],
    "V" : [0,1]
}

# pitch_list = list(range(0,11))
# slant_list = [0,0.5,1,2,3,4,6,9]
# pitch_slant_combos = list(zip(pitch_list + [0]*len(slant_list),[0]*len(pitch_list) + slant_list))
# slant_name_list = ['0','05','1','2','3','4','6','9']
# slant_name_dict = {x : y for x, y in zip(slant_list, slant_name_list)}

scale_run_list = {
    # "0206" : 0.466,
    # "0553" : 1.25,
    "1000" : 2.26365,
    # "1588" : 3.6,
}


for wing_pos in wing_pos_list:
    for scale, scale_factor in scale_run_list.items():
        for pol in pol_run_dict.keys():

                
                PROJECT_PATH = r'E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\parameterised\replace_wing\parameterised\\' + f"Bernard_rw_{wing_pos}_thicker_rotated_0250"
                SYMB_PATH = PROJECT_PATH + '.SMB'

                SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)
                SymbolsList.SetSymbolByName("Ephi", pol_run_dict[pol][0])
                SymbolsList.SetSymbolByName("Etheta", pol_run_dict[pol][1])
                SymbolsList.SetSymbolByName("Scale", scale_factor)
                SymbolsList.SetSymbolByName("f", f)
                SymbolsList.SetSymbolByName("ReBody", ReBody)
                SymbolsList.SetSymbolByName("ImBody", ImBody)
                SymbolsList.SetSymbolByName("ReChitin", ReChitin)
                SymbolsList.SetSymbolByName("ImChitin", ImChitin)
                SymbolsList.SetSymbolByName("pitch", 0)
                SymbolsList.SetSymbolByName("slant", 0)


                pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

                
                print(f"Running {wing_pos} {scale} {pol} {0} {0}run")
                SymbolsList.PrintSymbols()

                BASE_FILE_NAME = f"Bernard_dummy_wing_parameterised_{frequency_name}_{pol}_{wing_pos}_{scale}_p{0}_s{0})"
                SAVE_PATH = r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\parameterised\replace_wing\low_frequency\\"


                # Capture the output of PrintSymbols
                output = io.StringIO()
                sys.stdout = output
                SymbolsList.PrintSymbols()
                sys.stdout = sys.__stdout__

                with open(SAVE_PATH + r'\log_files\\' + f"{BASE_FILE_NAME}_symbol_log.txt", "w") as file:
                    file.write(output.getvalue())

                pro.Run(PROJECT_PATH)

                far_field = wiplpy.WResults.InitializeFFResults(PROJECT_PATH)

                theta = far_field.GetThetaPoints()[0]
                frequency = far_field.GetFrequencies()[0]

                results_extractor = FFObjToDictConverter(far_field, theta, frequency)
                results_extractor.save_output_dict(SAVE_PATH + f"{BASE_FILE_NAME}_dict.pkl")