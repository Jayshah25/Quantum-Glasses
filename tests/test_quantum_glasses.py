import quantum_glasses
import unittest

class TestQuantumGlasses(unittest.TestCase):

    def test_main(self):
        self.assertEqual(quantum_glasses.main(),True)