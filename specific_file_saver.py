import wiplpy.WiplInterface
import wiplpy.WResults
import wiplpy.WSymbols as symb
from FFObjToDict import FFObjToDictConverter

PATH_LIST = [
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\H\C_band\Bernard_12_Full_M_0250_1000_H_056",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\C_band\Bernard_12_Full_M_0250_1000_V_056",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\H\X_band\Bernard_12_Full_M_0250_1000_H_094_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\X_band\Bernard_12_Full_M_0250_1000_V_094_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid_top\1000\H\Ellipsoid_H_1000_94",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid_top\1000\V\Ellipsoid_V_1000_94",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\Bernard_12_Full_M_0250_1000_V_027_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\0553\H\Bernard_H_0250_0553_027",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\0206\H\Bernard_H_0250_0206_020",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\0206\H\Bernard_H_0250_0206_037",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\090\Bernard_12_Full_M_0250_1000_V_090_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\120\Bernard_12_Full_M_0250_1000_V_120_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\160\Bernard_12_Full_M_0250_1000_V_160_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\220\Bernard_12_Full_M_0250_1000_V_220_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V\300\Bernard_12_Full_M_0250_1000_V_300_MirkLBG_ChenMeanandLegs",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid_top\1000\H\C_band\Ellipsoid_H_1000_056",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Ellipsoid_top\1000\V\C_band\Ellipsoid_V_1000_056",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V_high_res_no_leg_wing\027\Bernard_12_Full_M_0375_1000_027_no_leg_wing",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\V_no_leg\027\Bernard_12_Full_M_0250_1000_V_027_no_leg_wing"
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\H_low_res_no_leg\049\Bernard_H_0063_1000_049_no_leg",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\H_low_res_no_leg_wing\049\Bernard_H_0063_1000_049_no_leg_wing",
    # r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\H_low_res_no_wing\049\Bernard_H_0063_1000_049_no_wing",
    r"E:\Working_Copy\Bernard_Ellipsoid_Comparison\Bernard_top\1000\H\049\Bernard_12_Full_M_0250_1000_H_049"
]

SAVE_PATH_LIST = [
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\H_DICT_PKL\Bernard_0250_1000_H_056.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_056.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\H_DICT_PKL\Bernard_0250_1000_H_094.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_094.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Ellipsoid_run_outputs\1000\H_DICT_PKL\Ellipsoid_1000_H_094.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Ellipsoid_run_outputs\1000\V_DICT_PKL\Ellipsoid_1000_V_094.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_12_Full_M_0250_1000_V_027.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\0206\H_DICT_PKL\Bernard_H_0250_0206_020",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\0206\H_DICT_PKL\Bernard_H_0250_0206_037",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\0553\H_DICT_PKL\Bernard_H_0250_0553_027",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_090.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_120.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_160.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_220.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_300.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Ellipsoid_run_outputs\1000\H_DICT_PKL\Ellipsoid_1000_H_056.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Ellipsoid_run_outputs\1000\V_DICT_PKL\Ellipsoid_1000_V_056.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0375_1000_V_027_no_leg_wing.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\V_DICT_PKL\Bernard_0250_1000_V_027_no_leg_wing.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\H_DICT_PKL_low_res\Bernard_0063_1000_V_049_no_leg.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\H_DICT_PKL_low_res\Bernard_0063_1000_V_049_no_leg_wing.pkl",
    # r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\H_DICT_PKL_low_res\Bernard_0063_1000_V_049_no_wing.pkl",
    r"C:\Users\NCAS\Documents\Tommy\Bernard_run_outputs\1000\H_DICT_PKL\Bernard_0250_1000_H_049.pkl"

]

WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"
pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

for PATH, SAVE_PATH in zip(PATH_LIST, SAVE_PATH_LIST):
    print(PATH)
    far_field = wiplpy.WResults.InitializeFFResults(PATH)

    theta = far_field.GetThetaPoints()[0]
    frequencies = far_field.GetFrequencies()

    frequency = frequencies[0]
    print('Saving frequncy:', frequency)
    results_extractor = FFObjToDictConverter(far_field, theta, frequency)
    results_extractor.save_output_dict(SAVE_PATH)

    print('Saved:', SAVE_PATH)
