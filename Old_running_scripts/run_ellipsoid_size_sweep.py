import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter

import io
import os
import sys

# set up to run parameterised ellipsoid at 10 degree pitch
 
WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"



frequency_name = '560'
f = 5.6
ReBody = 43
ImBody = 19


pol_run_dict = {
    "H" : [1,0],
    "V" : [0,1]
}

# PITCH = 10

# pitch_list = list(range(0,9))
# slant_list = [0,0.5,1,2,3,4,6,9]
# pitch_slant_combos = list(zip(pitch_list + [0]*len(slant_list),[0]*len(pitch_list) + slant_list))
# slant_name_list = ['0','05','1','2','3','4','6','9']
# slant_name_dict = {x : y for x, y in zip(slant_list, slant_name_list)}

scale_run_list = { # moth length in mm
    "0206" : 3.5,
    "0553" : 9.4,
    "1000" : 17,
    "1588" : 27,
}


for scale, scale_factor in scale_run_list.items():
    for PITCH in [0,10]:
        for pol in pol_run_dict.keys():
            PROJECT_PATH = r'E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid_top\parameterised\\' + f"Ellipsoid_parameterised"
            SYMB_PATH = PROJECT_PATH + '.SMB'

            SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)
            SymbolsList.SetSymbolByName("Ephi", pol_run_dict[pol][0])
            SymbolsList.SetSymbolByName("Etheta", pol_run_dict[pol][1])
            SymbolsList.SetSymbolByName("moth_length", scale_factor)
            SymbolsList.SetSymbolByName("f", f)
            SymbolsList.SetSymbolByName("ReBody", ReBody)
            SymbolsList.SetSymbolByName("ImBody", ImBody)
            SymbolsList.SetSymbolByName("pitch", PITCH) # have set pitch to 10 degrees
            SymbolsList.SetSymbolByName("slant", 0)


            pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

            
            print(f"Running {scale} {pol} run")
            SymbolsList.PrintSymbols()

            BASE_FILE_NAME = f"Ellipsoid_parameterised_{frequency_name}_{pol}_{scale}_p{PITCH}_s{0}"
            SAVE_PATH = r"C:\Users\NCAS\Documents\Tommy\Ellipsoid_run_outputs\parameterised\size_analysis\\"


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