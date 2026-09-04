# test_tidelens.py
"""
Tests for TideLens module.
"""

import unittest
from tidelens import TideLens

class TestTideLens(unittest.TestCase):
    """Test cases for TideLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TideLens()
        self.assertIsInstance(instance, TideLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TideLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
