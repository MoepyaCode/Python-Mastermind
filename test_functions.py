import unittest
from unittest.mock import patch
from io import StringIO
import sys
import mastermind
from test_base import captured_io

class MyTestCase(unittest.TestCase):
    ''' 
    * Test case to test mastermind functionality.
    * This test case tests the functions individually.
    '''
    
    remove_prints = StringIO()
    sys.stdout = remove_prints 
    
    def test_code_generator(self):
        ''' 
        1. The random test code generator tests whether the code generates code\
            as it should.
        '''
        
        for i in range(100):
            code_generator = mastermind.create_code()
            self.assertEqual(len(code_generator), 4)
            self.assertFalse(type(code_generator) != type(list()))
            self.assertFalse(0 in code_generator,'Range 1 to 8')
            self.assertFalse(9 in code_generator,'Range 1 to 8')
            self.assertFalse(type(str) in code_generator, 'String in code!!!')
            
            
    def test_check_correctness(self):
        ''' 
        1. The test correctness checks if the function returns a boolean.
        '''
        
        self.assertFalse(mastermind.check_correctness(12, 4) != True)
        self.assertFalse(mastermind.check_correctness(12, 3) != False)
    
            
    @patch("sys.stdin", StringIO("123\nabc\n9999\n0000\nabcd\n1234\n"))
    def test_user_guess(self):
        ''' 
        1. The test user guess mocks the user input and tests the user\
            input using dummy values.
        '''
        
        user_input = mastermind.get_answer_input()
        self.assertEqual(user_input, "1234")
        self.assertFalse('9' in user_input or '0' in user_input)
    

    @patch("sys.stdin", StringIO("2143\n2244\n1234"))
    def test_take_turn(self):
        ''' 
        1. The test function checks if the program counts accordinly\
            specifically the correct digits in position and the correct\
            digits only.
        2. If the pragram created is not in accordance with the test\
            then the test will emit an error.
        '''
        
        self.assertEqual(mastermind.take_turn([1,2,3,4]), (0, 4))
        self.assertEqual(mastermind.take_turn([1,2,3,4]), (2, 0))
        self.assertEqual(mastermind.take_turn([1,2,3,4]), (4, 0))
        

if __name__ == '__main__':
    unittest.main()