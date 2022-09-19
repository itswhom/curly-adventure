import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('about to test a function')
        return super().setUp()

    def test_do_stuff(self):
        '''example comment that shows in command'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'dsf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self) -> None:
        print('cleaning up')
        return super().tearDown()
# this allows quick running of tests from commandline:
# python3 -m unittest -v
if __name__ == '__main__':
    # main here does not reference main.py, it means run all tests
    unittest.main()
