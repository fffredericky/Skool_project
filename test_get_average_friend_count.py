import unittest
import network_functions

class TestGetAverageFriendCount(unittest.TestCase):

    def test_get_average_empty(self):
        param = {}
        actual = network_functions.get_average_friend_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_get_average_one_person_one_friend(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_get_average_more_than_one_friend_one_person(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Claire Dunphy'], \
                 'Claire Dunphy': ['Phil Dunphy', 'Manny Delgado']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_average_more_than_one_friend_more_person(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_average_one_friend_each_more_person(self):
        param = {'Jay Pritchett': ['Gloria Pritchett'], 'Claire Dunphy': ['Phil Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)         
        
    def test_get_average_more_than_one_friend_each(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado', \
                                   'Claire Dunphy'], 'Claire Dunphy': ['Phil Dunphy', 'Jay Pritchett']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_get_multi_person_multi_friend(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado'], \
                 'Claire Dunphy': ['Phil Dunphy'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.6666666666666667
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

if __name__ == '__main__':
    unittest.main(exit=False)