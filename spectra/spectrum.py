# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:22:30 2024

@author: Örs
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


class Spectrum(object):
    def __init__(self, wavelength, profile, name='', label='Intensity', 
                 unit='Ph/s/'+r'$\Omega$'+'/nm'):
        
        if len(wavelength) != len(profile):
            raise ValueError('The <wavelength> and <profile> input is' 
                             'required to of the same size.')
        
        self.wavelength = np.array(wavelength)
        self.profile = np.array(profile)
        self.name = name
        self.label = label
        self.unit = unit
        self._set_interpolator()
        
    def _set_interpolator(self):
        self.interpolate = interp1d(self.wavelength, self.profile, 
                                    kind='quadratic', fill_value='extrapolate')        
            
    def show(self, xrange=None, yrange=None):
        plt.plot(self.wavelength, self.profile, 'r-', linewidth=3, 
                 label=self.name)
        plt.title('Spectrum for: '+ self.name, 
                  fontweight = 'bold', fontsize=12)
        plt.xlabel('Wavelength [nm]', fontweight = 'bold', fontsize=12)
        plt.ylabel(self.label + ' [' + self.unit + ']',
                   fontweight = 'bold', fontsize=12)
        if xrange is None:
            plt.xlim([self.wavelength.min(), self.wavelength.max()])
        else:
            plt.xlim(xrange)
        if yrange is None:
            plt.ylim([self.profile.min(), self.profile.max()])
        else:
            plt.ylim(yrange)
        plt.legend(fontsize=12, prop={'weight':'bold'}, edgecolor="inherit")
        plt.show()
        
class MultiSpectrum(object):
    def __init__(self, name=''):
        self.name=name
        
    def add_spectrum(self):
        pass
    
    def update_spectrum(self):
        pass
    
    def list_spectrum(self):
        pass
    
    def show_spectrum(self):
        pass