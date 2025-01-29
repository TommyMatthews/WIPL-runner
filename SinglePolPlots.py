import pandas as pd

import matplotlib.pyplot as plt

class SinglePolPlots:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def plot_corrected_rcs(self, title=None):
        phi = self.data['phi']
        corrected_rcs = self.data['Corrected_RCS']
        
        plt.figure(figsize=(8, 6))
        plt.plot(phi, corrected_rcs, label='Corrected RCS')
        plt.xlabel('Azimuth (degrees)')
        plt.ylabel('Corrected RCS (cm^2)')

        if title:
            plt.title(title)

        plt.legend()
        plt.show()