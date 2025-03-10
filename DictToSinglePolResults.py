import pandas as pd
#import WIPL_python_analysis
import pickle

class OutputDictToSinglePolResultsConverter:

    @classmethod
    def from_pickle(cls, file_path):
        with open(file_path, 'rb') as file:
            dict_results = pickle.load(file)
        return cls(dict_results)

    def __init__(self, dict_results):
        self.dict_results = dict_results
        self.theta = dict_results.pop("theta")
        self.frequency = dict_results.pop("frequency")
        self.wavelength = 30 / self.frequency

    def _convert_to_df(self):
        self.df = pd.DataFrame(self.dict_results)

    def _generate_additional_outuputs(self):
        self.df["Ephi"] = self.df["Re_Ephi"] + 1j * self.df["Im_Ephi"]
        self.df["Etheta"] = self.df["Re_Etheta"] + 1j * self.df["Im_Etheta"]
        self.df["Total_RCS"] = self.df["Total_RCS"]
        self.df["Corrected_RCS"] = self.df["Total_RCS"] * self.wavelength**2

    def generate_output_df(self):
        self._convert_to_df()
        self._generate_additional_outuputs()
        return self.df


if __name__ == "__main__":
    results = OutputDictToSinglePolResultsConverter.from_pickle(
        "X_H_alternate_run_dict.pkl"
    )
    df = results.generate_output_df()
    df.to_csv("X_H_alternate_run_df.csv")
