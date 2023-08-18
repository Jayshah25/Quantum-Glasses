from quantum_glasses import QuantumGlasses
import matplotlib
import unittest
import os

class TestQuantumGlasses(unittest.TestCase):

    def test_main(self):
        my_qglases = QuantumGlasses()

        if os.getenv('DISPLAY') is None:
            matplotlib.use('Agg')
            os.environ.__setitem__('DISPLAY', ':0.0')
            with self.assertRaises(Exception):
                self.assertEqual(my_qglases.main(testing=True), False)

        self.assertEqual(my_qglases.main(testing=True), True)
