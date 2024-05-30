# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:27:35 2024

@author: Örs
"""

import unittest
import numpy
from spectra.spectrum import Spectrum
from spectra.spectrum import MultiSpectrum

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
    EXPECTED_DELTA = 1e12
    
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
        self.assertIsInstance(self.spectrum.profile, numpy.ndarray, 
                              msg='Profile data is expected to be in '
                              'numpy.ndarray format.')
        for element in range(len(self.spectrum.profile)):
            self.assertEqual(self.spectrum.profile[element], 
                             self.EXPECTED_PROFILES[element], 
                             msg='Profile values dont match expected ones.')
    
    def test_interpolator(self):
        for element in range(len(self.EXPECTED_INTERPOLATION_INDEX)):
            self.assertAlmostEqual(self.spectrum.interpolate(self.EXPECTED_WAVELENGTH[element]), 
                             self.EXPECTED_PROFILES[element], 
                             msg='Interpolated values dont match expected ones.',
                             delta = self.EXPECTED_DELTA)
            
class MultiSpectrumTest(unittest.TestCase):
    
    INPUT_NAME = 'bes_spectrum'
    EXPECTED_ATTR = ['name', 'spectra']
    
    INPUT_WAVELENGTH = numpy.array([6560, 6561, 6562, 6563, 6564, 6565, 
                                    6566, 6567, 6568, 6569, 6570, 6571, 
                                    6572, 6573, 6574, 6575, 6576, 6577, 
                                    6578, 6579])
    INPUT_PROFILES = numpy.array([6.52185956e+15, 7.50898104e+15, 
                                  1.11625043e+16, 1.66442658e+16,
                                  2.02841119e+16, 2.04521145e+16, 
                                  2.14231774e+16, 2.88714057e+16,
                                  4.09192675e+16, 4.75669193e+16, 
                                  4.21983109e+16, 3.01976984e+16,
                                  2.19027901e+16, 2.04041686e+16, 
                                  2.04804396e+16, 1.72583136e+16,
                                  1.17628952e+16, 7.77056599e+15, 
                                  6.54854474e+15, 6.49523047e+15])
    INPUT_NAMES = ['test', 'test x 2', 'test x 3']
    
    def setUp(self):
        self.spectrum = MultiSpectrum(name=self.INPUT_NAME)
        
    def tearDown(self):
        del self.spectrum
        
    def test_necessary_attributes(self):
        for attr in self.EXPECTED_ATTR:
            assert hasattr(self.spectrum, attr)
    
    def test_spectrum_addition(self):
        self.spectrum.add_spectrum(self.INPUT_WAVELENGTH, self.INPUT_PROFILES, 
                                   self.INPUT_NAMES[0])
        self.assertListEqual(list(self.spectrum.spectra[self.INPUT_NAMES[0]].wavelength),
                             list(self.INPUT_WAVELENGTH), 
                             msg='The actual wavelength array does not match the expected wavelength in the added spectral object.')
        self.assertListEqual(list(self.spectrum.spectra[self.INPUT_NAMES[0]].profile),
                             list(self.INPUT_PROFILES), 
                             msg='The actual profile array does not match the expected profile in the added spectral object.')
    
    def test_spectrum_update(self):
        self.spectrum.add_spectrum(self.INPUT_WAVELENGTH, self.INPUT_PROFILES, 
                                   self.INPUT_NAMES[0])
        self.spectrum.update_spectrum(self.INPUT_NAMES[0], self.INPUT_WAVELENGTH, 
                                      self.INPUT_PROFILES*0, self.INPUT_NAMES[1])
        self.assertListEqual(list(self.spectrum.spectra[self.INPUT_NAMES[0]].wavelength),
                             list(self.INPUT_WAVELENGTH), 
                             msg='The actual wavelength array does not match the expected wavelength in the added spectral object.')
        self.assertListEqual(list(self.spectrum.spectra[self.INPUT_NAMES[0]].profile),
                             list(numpy.zeros(len(self.INPUT_PROFILES))), 
                             msg='The actual profile array does not match the expected profile in the added spectral object.')
    
    def test_spectrum_listing(self):
        for item in self.INPUT_NAMES:
            self.spectrum.add_spectrum(self.INPUT_WAVELENGTH, 
                                       self.INPUT_PROFILES, item)
        self.assertListEqual(self.INPUT_NAMES, self.spectrum.list_spectrum(),
                             msg='The spectral list does not match expected values.')
    
    def test_spectrum_comparison(self):
        pass
        