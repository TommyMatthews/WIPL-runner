import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter

import io
import os
import sys



WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

morpho_list = ['body'] #['body_wing', 'body_leg', 'body']
# morpho_list = ['body_wing_leg']
wing_pos_list = ['M'] # left out 'M' as already run


wing_pos = 'M'
morpho = 'body'

frequency_name_list = ['020', '027', '037', '049', '067', '090', '120', '160', '220', '300']
f_list = [2, 2.7, 3.7, 4.9, 6.7, 9.0, 12, 16, 22, 30]
ReBody_list = [47, 46, 44, 41, 40, 35, 30, 25, 20, 15]
ImBody_list = [20, 19, 19, 19, 19, 19, 19, 19, 19, 19]
ReChitin_list = [5.3, 5.2, 5.2, 5.1, 5.1, 5.0, 5.0, 4.9, 4.9, 4.8]
ImChitin_list = [0.11, 0.12, 0.12, 0.12, 0.12, 0.12, 0.13, 0.13, 0.13, 0.13]
f_info_list = list(zip(frequency_name_list, f_list, ReBody_list, ImBody_list, ReChitin_list, ImChitin_list))


pol_run_dict = {
    "H" : [1,0],
    "V" : [0,1]
}

# pitch_list = list(range(0,11))
slant_list = [0,0.5,1,2,3,4,6,9]
# pitch_slant_combos = list(zip(pitch_list + [0]*len(slant_list),[0]*len(pitch_list) + slant_list))
slant_name_list = ['0','05','1','2','3','4','6','9']
slant_name_dict = {x : y for x, y in zip(slant_list, slant_name_list)}

slant=0
pitch=0

scale_run_list = {
    "0206" : 0.466,
    "0553" : 1.25,
    "1000" : 2.26365,
    "1588" : 3.6,
}

counter = 0

for scale, scale_factor in scale_run_list.items():
    for pol in pol_run_dict.keys():
        for frequency_name, f, ReBody, ImBody, ReChitin, ImChitin in f_info_list:
            
                counter += 1

                PROJECT_PATH = r'E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\parameterised\\' + f"Bernard_0250_param_{wing_pos}_{morpho}"
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
                SymbolsList.SetSymbolByName("pitch", pitch)
                SymbolsList.SetSymbolByName("slant", slant)


                pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

                print(f"Running run number {counter}")
                print(f"Running {wing_pos} {scale} {morpho} {pol} {pitch} {slant}run")
                SymbolsList.PrintSymbols()

                BASE_FILE_NAME = f"Bernard_parameterised_{frequency_name}_{pol}_{wing_pos}_{scale}_{morpho}_p{pitch}_s{slant_name_dict[slant]}"
                SAVE_PATH = r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\parameterised\\size_frequency_analysis\\"


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