import unittest
import script

class TestGame(unittest.TestCase):
    def test_input(self): # guess, answer
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.run_guess(3, 7)
        self.assertFalse(result)
    
    def test_input_wrong_number(self):
        result = script.run_guess(11, 5)
        self.assertFalse(result)
    
    def test_input_string(self):
        result = script.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
    