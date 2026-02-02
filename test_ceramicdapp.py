# test_ceramicdapp.py
"""
Tests for CeramicDapp module.
"""

import unittest
from ceramicdapp import CeramicDapp

class TestCeramicDapp(unittest.TestCase):
    """Test cases for CeramicDapp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CeramicDapp()
        self.assertIsInstance(instance, CeramicDapp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CeramicDapp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
