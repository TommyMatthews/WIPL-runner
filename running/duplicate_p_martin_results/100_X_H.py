import wiplpy.WiplInterface
import wiplpy.WResults
import WIPL_PYTHON_ANALYSIS
import joblib

PROJECT_PATH = r"C:\Users\NCAS\Documents\Tommy\purple_martin_work\P_Martin2\X_band\horizontal_alternate_run\M_Wing_1_100_H_X"
WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024"

pro = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldpro")

print("Starting run")
pro.Run(PROJECT_PATH)
print("Run complete")

print("Initialising far field results")
far_field = wiplpy.WResults.InitializeFFResults(PROJECT_PATH)
print("Saving far field results")

joblib.dump(far_field, "100_X_H.pkl")




