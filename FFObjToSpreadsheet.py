import pandas as pd
import wiplpy.WResults
import pickle

class ResultsExtractor():

    def __init__(self, ffobject, theta, frequency):
        self.ffobject = ffobject
        self.theta = theta
        self.frequency = frequency

    def extract_phi_results(self):
        re_Ephi = self.ffobject.GetYData('Phi-component',"Re", XaxisLabel='phi',Cuts ={"Theta" : self.theta, "Frequency" : self.frequency,"Excitation" : 1})
        im_Ephi = self.ffobject.GetYData('Phi-component',"Im", XaxisLabel='phi',Cuts ={"Theta" : self.theta, "Frequency" : self.frequency,"Excitation" : 1})
        
        return re_Ephi, im_Ephi
    
    def extract_theta_results(self):
        re_Etheta = self.ffobject.GetYData('Theta-component',"Re", XaxisLabel='phi',Cuts ={"Theta" : self.theta, "Frequency" : self.frequency,"Excitation" : 1})
        im_Etheta = self.ffobject.GetYData('Theta-component',"Im", XaxisLabel='phi',Cuts ={"Theta" : self.theta, "Frequency" : self.frequency,"Excitation" : 1})
        
        return re_Etheta, im_Etheta

    def correct_rcs(self, rcs):
        wavelength = 30 / self.frequency
        corrected_rcs = rcs * wavelength**2
        return corrected_rcs 

    def extract_total_rcs(self):
        total_rcs = self.ffobject.GetYData('Total',"RCS", XaxisLabel='phi',Cuts ={"Theta" : self.theta, "Frequency" : self.frequency,"Excitation" : 1})
        corrected_rcs = self.correct_rcs(total_rcs)
        return total_rcs, corrected_rcs
    
    def generate_output_df(self):

        re_Ephi, im_Ephi = self.extract_phi_results()
        re_Etheta, im_Etheta = self.extract_theta_results()
        Ephi = re_Ephi + j*im_Ephi
        Etheta = re_Etheta + j*im_Etheta

        total_rcs, corrected_rcs = self.extract_total_rcs()

        output_df = pd.DataFrame({
            'phi': self.ffobject.GetPhiPoints(),
            'Re_Ephi': re_Ephi,
            'Im_Ephi': im_Ephi,
            'Re_Etheta': re_Etheta,
            'Im_Etheta': im_Etheta,
            'Total_RCS': total_rcs,
            'Corrected_RCS': corrected_rcs
        })

        output_df.attrs['theta'] = self.theta
        output_df.attrs['frequency'] = self.frequency

        return output_df
if __name__ == "__main__":
    with open('X_V_alternate_run_results.pkl', 'rb') as file:
        ffobject = pickle.load(file)

    theta = ffobject.GetThetaPoints()[0]
    frequency = ffobject.GetFrequencies()[0]

    results_extractor = ResultsExtractor(ffobject, theta, frequency)

    results_extractor.generate_output_df().to_csv('X_V_test.csv')
