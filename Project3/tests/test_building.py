'''test the building class'''

import unittest
import pytest
import logging
logger = logging.Logger('mylogger', level=logging.INFO)

def fun(x):
    return x + 1

class TestBuilding(unittest.TestCase):

    def setUp(self):
        ## self.mysetup = 'setup done'
        logging.info("setup done!")
        print("setup done")

    @pytest.mark.materialtest
    def test_material(self):
        self.assertEqual(fun(3), 4)

    @pytest.mark.skip("Do not run this")
    def test_key(self):
        
        a = ['a', 'b']
        b = ['b'] 
        c = ['3']
        assert a == b