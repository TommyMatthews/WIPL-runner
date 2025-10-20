import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter
from wavelength_sweep_generator import generate_wavelength_shifts

import io
import os
import sys



WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

coord_file_code = "10_20_100_30"

frequency_name = '056'
f = 5.6
ReBody = 43
ImBody = 19
scale=1000
scale_factor=17


pol_run_dict = {
    "H" : [1,0],
    "V" : [0,1]
}

PROJECT_PATH = r"E:\Working_Copy\Multi_moth_simulations\spatial_shift\Ellipsoid_x_shift"

coordinates = generate_wavelength_shifts(f)
counter = 0

for coordinate in coordinates:
    for pol in pol_run_dict.keys():

        SYMB_PATH = PROJECT_PATH + '.SMB'

        SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)
        SymbolsList.SetSymbolByName("Ephi", pol_run_dict[pol][0])
        SymbolsList.SetSymbolByName("Etheta", pol_run_dict[pol][1])
        SymbolsList.SetSymbolByName("moth_length", scale_factor)
        SymbolsList.SetSymbolByName("f", f)
        SymbolsList.SetSymbolByName("ReBody", ReBody)
        SymbolsList.SetSymbolByName("ImBody", ImBody)
        SymbolsList.SetSymbolByName("pitch", 0)
        SymbolsList.SetSymbolByName("slant", 0)
        SymbolsList.SetSymbolByName("x_shift", coordinate)

        pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

        SymbolsList.PrintSymbols()

        BASE_FILE_NAME = f"Ellipsoid_shift_{frequency_name}_x{counter}_{pol}"
        SAVE_PATH = r"C:\Users\NCAS\Documents\Tommy\multi_moth_outputs\x_shift_tests\ellipsoids\\"


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

    counter +=1 