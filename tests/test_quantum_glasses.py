from quantum_glasses import QuantumGlasses
import matplotlib
import unittest
import os

class TestQuantumGlasses(unittest.TestCase):

    def test_main(self):
        if os.getenv('DISPLAY') is None:
            matplotlib.use('Agg')

        my_qglases = QuantumGlasses()
        self.assertEqual(my_qglases.main(testing=True), True)
