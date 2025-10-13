import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter
import time
import csv
import io
import os
import sys



WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

start = time.time()


pol_run_dict = {
    "H" : [1,0],
    "V" : [0,1]
}

# slant = 0.4
# pitch_list = [-25,-20,-15,-10,-5,0,5,10,15,20,25]
# aspect_ratio_list = [1.6,1.8,2.0,2.2,2.4]
FREQUENCY = 5.6
length_mm = [2,8,10,12,14,16,30]
# BODY_RE = 56
# BODY_IM = 15


PROJECT_PATH = r"C:\Users\NCAS\Documents\Tommy\Sketchfab_hoverfly\exports\Syrphus_ribesii_body_only0400"
SYMB_PATH = PROJECT_PATH + '.SMB'

SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)

#PROJECT_PATH = r"E:\Working_Copy\MeteoFrance\prelimnary_work\bird_speroid"

pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

# for semi_major_axis in semi_major_axes:
#     for pitch in pitch_list:
#         for aspect_ratio in aspect_ratio_list:

SymbolsList.SetSymbolByName("pitch", 0)
SymbolsList.SetSymbolByName("slant", 0)
SymbolsList.SetSymbolByName("f", FREQUENCY)


for size in length_mm:
    for pol in pol_run_dict:

        SymbolsList.SetSymbolByName("Ephi", pol_run_dict[pol][0])
        SymbolsList.SetSymbolByName("Etheta", pol_run_dict[pol][1])
        SymbolsList.SetSymbolByName("length_mm", size)


        
        print(f"Running {pol} run")
        SymbolsList.PrintSymbols()

        BASE_FILE_NAME = f"hoverfly_0400_p0_s0_{pol}_L{size}"
        SAVE_PATH = r"C:\Users\NCAS\Documents\Tommy\Sketchfab_hoverfly\results\\"


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
    
end = time.time()
print(f'Time taken for hoverfly test {end-start:.4f} s')