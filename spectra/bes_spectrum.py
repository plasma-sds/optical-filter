# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:28:27 2024

@author: Örs
"""

from spectra.spectrum import MultiSpectrum

class BeamEmissionSpectrum(object):
    def __init__(self, name=''):
        self.name = name
        self.background = MultiSpectrum(name='Background Spectra')
        self.cx = MultiSpectrum(name='Charge Exchange Spectra')
        self.bes = MultiSpectrum(name='Active Emission Spectra')
        self.total = MultiSpectrum(name='Total Spectra')
        self.filter = None
        
    def add_filter(self, optical_filter):
        self.filter = optical_filter
        
    def list_spectrum(self):
        return (list(self.background.keys()) + list(self.cx.keys()) + 
                list(self.bes.keys()) + list(self.total.keys()))
        
    def show_spectra(self, yaxis='normal', xrange=None, yrange=None, background=True,
                     cx=False, bes=True, total=False):
        pass