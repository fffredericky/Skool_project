import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_one_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_get_families_multi_person_one_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett'], 'Claire Dunphy': ['Phil Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire', 'Phil'], 'Pritchett': ['Gloria', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 

    def test_get_families_multi_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Manny Delgado'], 'Manny Delgado': ['Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Delgado': ['Manny'], 'Dunphy': ['Luke']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_get_families_one_person_multi_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Mitchell Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_get_families_one_person_multi_friend_diff_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     
        
    def test_get_families_multi_person_multi_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Mitchell Pritchett'], \
                 'Gloria Pritchett': ['Mitchell Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_multi_person_multi_friend_diff_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado'], \
                 'Claire Dunphy': ['Phil Dunphy'], 'Manny Delgado': ['Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay'], 'Delgado': ['Manny'], \
                    'Dunphy': ['Claire', 'Luke', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
        
if __name__ == '__main__':
    unittest.main(exit=False)