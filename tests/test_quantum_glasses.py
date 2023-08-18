from quantum_glasses import QuantumGlasses
import unittest
import os

class TestQuantumGlasses(unittest.TestCase):

    def test_main(self):
        """Global test."""
        my_qglases = QuantumGlasses()

        if os.getenv('DISPLAY') is None:
            with self.assertRaises(Exception):
                my_qglases.main(testing=True)

        self.assertEqual(my_qglases.main(testing=True), True)
