from quantum_glasses import QuantumGlasses
import unittest

class TestQuantumGlasses(unittest.TestCase):

    def test_main(self):
        my_qglases = QuantumGlasses()
        self.assertEqual(my_qglases.main(), True)
