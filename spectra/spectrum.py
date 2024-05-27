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
            
    def show(self, xrange=None, yrange=None, points=None):
        plt.plot(self.wavelength, self.profile, 'r-', linewidth=2, 
                 label=self.name)
        if not points is None:
            plt.scatter(np.array(points), self.interpolate(np.array(points)), 
                        s=30, label='Interpolated points', 
                        marker='x', linewidths=2, c='b')
        
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
        self.spectra = {}
        
    def add_spectrum(self, wavelength, profile, name, label='Intensity', 
                 unit='Ph/s/'+r'$\Omega$'+'/nm'):
        self.spectra[name] = Spectrum(wavelength, profile, name=name,
                                             label=label, unit=unit)
    
    def update_spectrum(self, reference, wavelength, profile, name, 
                        label='Intensity', unit='Ph/s/'+r'$\Omega$'+'/nm'):
        if reference in self.list_spectrum():
            self.spectra[reference] = Spectrum(wavelength, profile, name, 
                                               label='Intensity', 
                                               unit='Ph/s/'+r'$\Omega$'+'/nm')
        else:
            raise KeyError('The expected key: '+ reference + ' is not present.')
    
    def list_spectrum(self):
        return list(self.spectra.keys())
    
    def compare_spectra(self, actual, reference, kind='absolute'):
        val = self.spectra[actual].profile - self.spectra[reference].interpolate(self.spectra[actual].wavelength)
        if kind == 'absolute':
            return val
        elif kind == 'relative':
            return val/self.spectra[reference].interpolate(self.spectra[actual].wavelength)
        else:
            print('The comparison: ' + kind + ' is not supported.')
    
    def show_spectra(self, yaxis='normal', xrange=None, 
                     yrange=None, selection=None):
        if selection is None:
            plots = self.list_spectrum()
        else:
            plots=list(selection)
        for plot in plots:
            try:
                plt.plot(self.spectra[plot].wavelength, self.spectra[plot].profile,
                         linewidth=2, label=self.spectra[plot].name)
            except KeyError:
                print('The requested plot: ' + plot + 'is not avaiable.')
        plt.title('Spectrum for: '+ self.name, 
                  fontweight = 'bold', fontsize=12)
        plt.xlabel('Wavelength [nm]', fontweight = 'bold', fontsize=12)
        plt.ylabel(self.spectra[plot].label + ' [' + self.spectra[plot].unit + ']',
                   fontweight = 'bold', fontsize=12)
        if xrange is not None:
            plt.xlim(xrange)
        if yrange is not None:
            plt.ylim(yrange)
        plt.legend(fontsize=12, prop={'weight':'bold'}, edgecolor="inherit")
        plt.show()    