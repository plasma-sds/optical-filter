# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:22:30 2024

@author: Örs
"""

import numpy as np
import matplotlib.pyplot as plt


class Spectrum(object):
    def __init__(self, wavelength, profile, 
                 name='', label='Intensity', 
                 unit='Ph/s/nm'):
        
        if len(wavelength) == len(profile):
            self.wavelength = np.array(wavelength)
            self.profile = np.array(profile)
            self.name = name
            self.label = label
            self.unit = unit
            
    def show():
        plt.plot(self.wavelength, self.profile)
        plt.show()