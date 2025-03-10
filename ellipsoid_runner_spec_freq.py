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
    # "1000",
    "0553",
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

            PATH = F"E:\\Working_Copy\\Bernard_Ellipsoid_Comparison\\Ellipsoid_top\\{scale}\\{pol}_low_res\\{freq}\\Ellipsoid_{pol}_{scale}_{freq}"
            # PATH = F"E:\\Working_Copy\\Bernard_Ellipsoid_Comparison\\Ellipsoid_top\\{scale}\\{pol}\\{freq}\\Ellipsoid_{pol}_{scale}_{freq}"

            BASE_FILE_NAME = f"Ellipsoid_{scale}_sweep_{pol}_{freq}"
            SAVE_PATH = f"C:\\Users\\NCAS\\Documents\\Tommy\\Ellipsoid_run_outputs\\{scale}\\{pol}_DICT_PKL_low_res_comp\\"

            # pro.Run(PATH)

            far_field = wiplpy.WResults.InitializeFFResults(PATH)

            theta = far_field.GetThetaPoints()[0]
            frequencies = far_field.GetFrequencies()

            frequency = frequencies[0]
            print('Saving frequncy:', frequency)
            results_extractor = FFObjToDictConverter(far_field, theta, frequency)
            results_extractor.save_output_dict(SAVE_PATH + f"{BASE_FILE_NAME}_dict.pkl")
