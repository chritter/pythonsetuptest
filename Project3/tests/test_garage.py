''' test the garage class'''
import unittest
import pytest
import logging
#logging.Logger('mylogger', level=logging.INFO)
LOGGER = logging.getLogger(__name__)

from .context import garage

# autouse=True, scope='module', params=['stone', 'wood'])

@pytest.fixture
def setup1(request):
    return garage.Garage(request.param)

@pytest.fixture
def setup2():
    return garage.Garage('wood')

class TestGarage():

    # here two tests are spanned, stone and wood are input parameter to the
    # setup fixture
    @pytest.mark.parametrize('setup1', ['stone', 'wood'], indirect=['setup1'])
    def test_car_door(self, setup1):
        LOGGER.info('test log: '+setup1.car_door('whiteroof'))
        assert 'whiteroof' in setup1.car_door('whiteroof')

    # simple setup
    @pytest.fixture(autouse=True)
    def _setup2(self):
        self.setup2 = garage.Garage('wood')

    @pytest.mark.parametrize('paint_color', ['red', 'blue'])
    def test_coloring(self, paint_color):
        assert self.setup2.coloring(paint_color)