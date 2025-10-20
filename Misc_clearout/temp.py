import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols
from FFObjToDict import FFObjToDictConverter


PROJECT_PATH = r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid\ellipsoid"
SYMB_PATH = r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid\ellipsoid.SMB"


WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"


pol_run_list = {
    "H" : [1,0],
    "V" : [0,1]
}

scale_run_list = {
    "0375" : [0.375],
    "1000" : [1.00],
}


for scale, scale_factor in scale_run_list.items():
    for pol, values in pol_run_list.items():

        SymbolsList = wiplpy.WSymbols.GetSymbols(SYMB_PATH)
        SymbolsList.SetSymbolByName("Ephi", values[0])
        SymbolsList.SetSymbolByName("Etheta", values[1])
        SymbolsList.SetSymbolByName("Scale", scale_factor[0])


        pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

        
        print(f"Running {scale} {pol} run")
        SymbolsList.PrintSymbols()

        BASE_FILE_NAME = f"Ellipsoid_{scale}_{pol}"
        SAVE_PATH = f"C:\\Users\\NCAS\\Documents\\Tommy\\symbol_testing\\"



        pro.Run(PROJECT_PATH)

        far_field = wiplpy.WResults.InitializeFFResults(PROJECT_PATH)

        theta = far_field.GetThetaPoints()[0]
        frequencies = far_field.GetFrequencies()

        if len(frequencies) > 1:
            print("Multiple frequencies present")
            for counter, frequency in enumerate(far_field.GetFrequencies()):
                print(f"Saving frequency number {counter}, value {frequency} GHz")
                results_extractor = FFObjToDictConverter(far_field, theta, frequency)
                results_extractor.save_output_dict(
                    SAVE_PATH + f"{BASE_FILE_NAME}_f{counter}_dict.pkl"
                )

        else:
            print("Only one frequency present")
            frequency = frequencies[0]
            results_extractor = FFObjToDictConverter(far_field, theta, frequency)
            results_extractor.save_output_dict(SAVE_PATH + f"{BASE_FILE_NAME}_dict.pkl")
