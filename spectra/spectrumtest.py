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
    
    EXPECTED_ATTR = ['wavelength', 'profile', 'name',
                     'interpolate', 'label', 'unit']
    EXPECTED_WAVELENGTH = numpy.array([6560, 6561, 6562, 6563, 6564, 6565, 
                                       6566, 6567, 6568, 6569, 6570, 6571, 
                                       6572, 6573, 6574, 6575, 6576, 6577, 
                                       6578, 6579])
    EXPECTED_PROFILES = numpy.array([6.52185956e+15, 7.50898104e+15, 
                                     1.11625043e+16, 1.66442658e+16,
                                     2.02841119e+16, 2.04521145e+16, 
                                     2.14231774e+16, 2.88714057e+16,
                                     4.09192675e+16, 4.75669193e+16, 
                                     4.21983109e+16, 3.01976984e+16,
                                     2.19027901e+16, 2.04041686e+16, 
                                     2.04804396e+16, 1.72583136e+16,
                                     1.17628952e+16, 7.77056599e+15, 
                                     6.54854474e+15, 6.49523047e+15])
    EXPECTED_INTERPOLATION_INDEX = numpy.array([0, 3, 7])
    
    def setUp(self):
        self.spectrum = Spectrum(self.EXPECTED_WAVELENGTH, 
                                 self.EXPECTED_PROFILES)

    def tearDown(self):
        del self.spectrum
        
    def test_necessary_attributes(self):
        for attr in self.EXPECTED_ATTR:
            assert hasattr(self.spectrum, attr)
    
    def test_wavelength(self):
        self.assertIsInstance(self.spectrum.wavelength, numpy.ndarray, 
                              msg='Wavelength data is expected to be in '
                              'numpy.ndarray format.')
        for element in range(len(self.spectrum.wavelength)):
            self.assertEqual(self.spectrum.wavelength[element], 
                             self.EXPECTED_WAVELENGTH[element], 
                             msg='Wavelength values dont match expected ones.')
    
    def test_profile(self):
        pass
    
    def test_interpolator(self):
        pass