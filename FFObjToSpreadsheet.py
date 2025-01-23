import pandas as pd
import wiplpy.WResults
import pickle

class ResultsExtractor():

    def __init__(self, ffobject, theta, frequency):
        self.ffobject = ffobject
        self.theta = theta
        self.frequency = frequency

    def extract_phi_results(self):
        "Returns complex phi results"
        pass
    
    def extract_theta_results(self):
        "Returns complex theta results"
        pass

    #also do total RCS 

    #generate output df with all of these

with open('X_V_alternate_run_results.pkl', 'rb') as file:
    ffobject = pickle.load(file)