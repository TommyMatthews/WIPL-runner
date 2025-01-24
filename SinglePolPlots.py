import pandas as pd

import matplotlib.pyplot as plt

class SinglePolPlots:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
    
    def plot(self):
        phi = self.data['phi']
        ephi = self.data['Ephi']
        etheta = self.data['Etheta']
        corrected_rcs = self.data['Corrected RCS']
        
        plt.figure(figsize=(12, 8))
        
        plt.subplot(3, 1, 1)
        plt.plot(phi, ephi, label='Ephi')
        plt.xlabel('Phi')
        plt.ylabel('Ephi')
        plt.legend()
        
        plt.subplot(3, 1, 2)
        plt.plot(phi, etheta, label='Etheta')
        plt.xlabel('Phi')
        plt.ylabel('Etheta')
        plt.legend()
        
        plt.subplot(3, 1, 3)
        plt.plot(phi, corrected_rcs, label='Corrected RCS')
        plt.xlabel('Phi')
        plt.ylabel('Corrected RCS')
        plt.legend()
        
        plt.tight_layout()
        plt.show()

def plot_ephi(self):
    phi = self.data['phi']
    ephi = self.data['Ephi']
    
    plt.figure(figsize=(8, 6))
    plt.plot(phi, ephi, label='Ephi')
    plt.xlabel('Phi')
    plt.ylabel('Ephi')
    plt.legend()
    plt.show()

def plot_etheta(self):
    phi = self.data['phi']
    etheta = self.data['Etheta']
    
    plt.figure(figsize=(8, 6))
    plt.plot(phi, etheta, label='Etheta')
    plt.xlabel('Phi')
    plt.ylabel('Etheta')
    plt.legend()
    plt.show()

def plot_corrected_rcs(self):
    phi = self.data['phi']
    corrected_rcs = self.data['Corrected RCS']
    
    plt.figure(figsize=(8, 6))
    plt.plot(phi, corrected_rcs, label='Corrected RCS')
    plt.xlabel('Phi')
    plt.ylabel('Corrected RCS')
    plt.legend()
    plt.show()