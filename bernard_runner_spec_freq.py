import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols as symb
from FFObjToDict import FFObjToDictConverter

#PROJECT_PATH = r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Corrected_Bernard\LepidopteraNoctuidaeMoth_12_Full_M_0250_0375_94_MirkLBG_ChenMeanandLegs"

WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

pol_run_list = [
    # "H",
    "V" 
]

scale_run_list = [
    "1000",
    # "0553",
    # "0206",
    # "1588",
]

freq_run_list = [
    '020',
    '027',
    '037',
    '049',
    '067',
    '090',
    '120',
    '160',
    '220',
    '300',
]

pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

for scale in scale_run_list:
    for pol in pol_run_list:
        for freq in freq_run_list:

            print("Running", scale, pol, freq, "run")

            # PATH = F"E:\\Working_Copy\\Bernard_Ellipsoid_Comparison\\Bernard_top\\{scale}\\{pol}\\{freq}\\Bernard_12_full{pol}_0063_{scale}_{freq}"
            PATH = F"E:\\Working_Copy\\Bernard_Ellipsoid_Comparison\\Bernard_top\\{scale}\\{pol}_no_leg\\{freq}\\Bernard_12_Full_M_0250_1000_V_{freq}_no_leg"

            # BASE_FILE_NAME = f"Bernard_{scale}_sweep_{pol}_{freq}"
            BASE_FILE_NAME = f"Bernard_0250_{scale}_sweep_{pol}_{freq}_no_leg"
            SAVE_PATH = f"C:\\Users\\NCAS\\Documents\\Tommy\\Bernard_run_outputs\\{scale}\\{pol}_DICT_PKL\\"

            # pro.Run(PATH)

            far_field = wiplpy.WResults.InitializeFFResults(PATH)

            theta = far_field.GetThetaPoints()[0]
            frequencies = far_field.GetFrequencies()

            frequency = frequencies[0]
            print('Saving frequncy:', frequency)
            results_extractor = FFObjToDictConverter(far_field, theta, frequency)
            results_extractor.save_output_dict(SAVE_PATH + f"{BASE_FILE_NAME}_dict.pkl")
