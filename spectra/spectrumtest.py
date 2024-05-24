# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:27:35 2024

@author: Örs
"""

import unittest
import numpy
import scipy
from spectra.spectrum import Spectrum

class SpectrumTest(unittest.TestCase):

    
    def setUp(self):
        self.spectrum = Spectrum()

    def tearDown(self):
        del self.spectrum
        
    def test_necessary_attributes(self):
        pass
    
    def test_wavelength(self):
        pass
    
    def test_profile(self):
        pass
    
    def test_interpolator(self):
        pass