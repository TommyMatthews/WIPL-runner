import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter
from coord_parser import parse_csv

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

PROJECT_PATH = r"E:\Working_Copy\Multi_moth_simulations\ellipsoids_inital\Three_ellipsoids"

coordinates = parse_csv(f"three_bernard_coords_{coord_file_code}.csv")
counter = 0

for coordinate_row in coordinates:
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

        # Set the coordinates for the three ellipsoids
        for coord, coord_value in coordinate_row.items():
            SymbolsList.SetSymbolByName(coord, coord_value)

        pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

        SymbolsList.PrintSymbols()

        BASE_FILE_NAME = f"Three_ellipsoid_{frequency_name}_{coord_file_code}_row{counter}_{pol}"
        SAVE_PATH = r"C:\Users\NCAS\Documents\Tommy\multi_moth_outputs\three_ellipsoids\\"


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