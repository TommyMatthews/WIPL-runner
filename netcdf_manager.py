import xarray as xr
import numpy as np

def create_placeholder_dataset(initial_results, lengths, slants, pitches):

    phi = initial_results['phi']
    # Define scattering patterns
    scattering_patterns = ['H_H_r', 'H_H_i', 'H_V_r', 'H_V_i', 'V_H_r', 'V_H_i', 'V_V_r', 'V_V_i', 'Zdr', 'PhiDP', 'RCS_H_total', 'RCS_V_total', 'RCS_HH', 'RCS_VV', 'RCS_HV', 'RCS_VH']
    # Create the dataset with NaNs as placeholders
    data_vars = {
        pattern: (['length', 'pitch','slant', 'phi'],
                np.full((len(lengths), len(pitches), len(slants), len(phi)), np.nan))
        for pattern in scattering_patterns
    }
    # Create coordinates
    coords = {
        'length': lengths,
        'pitch': pitches,
        'slant': slants,
        'phi': phi
    }
    # Create the xarray Dataset
    ds = xr.Dataset(data_vars=data_vars, coords=coords) 

    ds.attrs['frequency'] = initial_results['frequency']
    ds.attrs['phi_counts'] = len(phi)

    return ds

def input_single_sim_results(ds, incident_pol, results_dict, kwargs):

    wavelength = 30/results_dict['frequency'] #cm

    ds[f'{incident_pol}_H_r'].loc[dict(**kwargs)] = results_dict['Re_Ephi']
    ds[f'{incident_pol}_H_i'].loc[dict(**kwargs)] = results_dict['Im_Ephi']
    ds[f'{incident_pol}_V_r'].loc[dict(**kwargs)] = results_dict['Re_Etheta']
    ds[f'{incident_pol}_V_i'].loc[dict(**kwargs)] = results_dict['Im_Etheta']
    ds[f'RCS_{incident_pol}_total'].loc[dict(**kwargs)] = np.array(results_dict['Total_RCS']) * (wavelength**2)
    ds[f'RCS_{incident_pol}H'].loc[dict(**kwargs)] = np.array(results_dict['phi_rcs']) * (wavelength**2)
    ds[f'RCS_{incident_pol}V'].loc[dict(**kwargs)] = np.array(results_dict['theta_rcs']) * (wavelength**2)

    return ds

def add_metadata(ds):

    for pol, pol_desc in zip(['H', 'V'], ['horizontal', 'vertical']):
        for pol_2, pol_desc_2 in zip(['H', 'V'], ['horizontal', 'vertical']):
            for re_im, re_im_desc in zip(['r', 'i'], ['Real', 'Imaginary']):
                var_name = f'{pol}_{pol_2}_{re_im}'
                ds[var_name].attrs['units'] = 'V/m'
                ds[var_name].attrs['description'] = f'{re_im_desc} component of the {pol_desc_2} scattered electric field for {pol_desc} incident radiation'

    # ds['Zdr'].attrs['units'] = 'dB'
    # ds['Zdr'].attrs['description'] = 'Differential reflectivity, ZDR, calculated as 10*log10(R), where R is the ratio of the resultant powers in the horizontal and vertical channels. 0 differential phase on transmission.'
    # ds['PhiDP'].attrs['units'] = 'degrees'
    # ds['PhiDP'].attrs['description'] = 'Differential phase, PhiDP, calculated as the phase difference between the horizontal and vertical channels. A simple de-aliasing function has been applied. 0 differential phase on transmission.'
    
    ds['length'].attrs['units'] = 'mm'
    ds['length'].attrs['description'] = 'length of model in mmm'

    ds['slant'].attrs['units'] = 'unitless'
    ds['slant'].attrs['description'] = 'Aspect ratio of the spheroid, defined as the ratio of the semi-major axis to the semi-minor axis'

    for pol, pol_desc in zip(['H', 'V'], ['horizontal', 'vertical']):
        for form, form_desc in zip(['H', 'V', '_total'], ['horizontal', 'vertical', 'total']):
            var_name = f'RCS_{pol}{form}'
            ds[var_name].attrs['units'] = 'cm^2'
            ds[var_name].attrs['description'] = f'{form_desc} measured radar cross section for {pol_desc} incident radiation'

    ds['pitch'].attrs['units'] = 'degrees'
    ds['pitch'].attrs['description'] = 'Pitch angle of the spheroid, defined as the angle between the along body axis and the horizontal plane'
    ds['phi'].attrs['units'] = 'degrees'
    ds['phi'].attrs['description'] = 'Azimuthal angle of the spheroid, defined as the angle between the along body axis and the x-axis in the horizontal plane'

    return ds