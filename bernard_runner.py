import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols as symb
from FFObjToDict import FFObjToDictConverter

#PROJECT_PATH = r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Corrected_Bernard\LepidopteraNoctuidaeMoth_12_Full_M_0250_0375_94_MirkLBG_ChenMeanandLegs"

WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

pol_run_list = {
    "H" : [1,0],
    "V" : [0,1]
}

scale_run_list = {
    # "0375" : [0.84886875],
    "1000" : [2.26365],
    "0553" : [],
    "0206" : [],
    "1588" : []
}

pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

for scale, scale_factor in scale_run_list.items():
    for pol, values in pol_run_list.items():

        print("Running", scale, pol, "run")

        PATH = F"E:\\Working_Copy\\Bernard_Ellipsoid_Comparison\\Bernard_top\\{scale}\\{pol}\\LepidopteraNoctuidaeMoth_12_Full_M_0250_0375_94_MirkLBG_ChenMeanandLegs"

        BASE_FILE_NAME = f"Bernard_{scale}_sweep_{pol}_1_60_20"
        SAVE_PATH = f"C:\\Users\\NCAS\\Documents\\Tommy\\Bernard_run_outputs\\{scale}\\{pol}_DICT_PKL\\"

        pro.Run(PATH)

        far_field = wiplpy.WResults.InitializeFFResults(PATH)

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
