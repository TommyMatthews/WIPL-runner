import wiplpy.WiplInterface
import wiplpy.WResults

PROJECT_PATH = r"C:\Users\NCAS\Documents\Tommy\analysis_code\WIPL-python-analysis\results_files\p_martin_duplicate\H_X\M_Wing_1_100_H_X"

# WIPLDInstallDirectory = r"C:\Program Files\WIPL-D\WIPL-D Pro 13.02.00"

# WIPLD = wiplpy.WiplInterface(WIPLDInstallDirectory, "wipldpro")

far_field = wiplpy.WResults.InitializeFFResults(PROJECT_PATH)

theta = far_field.GetThetaPoints()[0]
frequency = far_field.GetFrequencies()[0]

print(theta, frequency)
phi_results = far_field.GetPhiPoints()

# print(phi_results)

results_by_phi = far_field.GetYData(
    "Phi-component",
    "Re",
    XaxisLabel="phi",
    Cuts={"Theta": theta, "Frequency": frequency, "Excitation": 1},
)

print(results_by_phi)
# think I need to try this on a run that has been run using a built in set of excitations rather than a sweep.
