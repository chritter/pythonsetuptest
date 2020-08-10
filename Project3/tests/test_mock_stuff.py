# test_parameterized_fixture.py

from unittest import mock
from .context import garage


def test_mockonce():

    m = mock.Mock()

    m.some_method('foo', 'bar')

    m.some_method.assert_called_once_with('foo', 'bar')


def test_replace():
    """
    Replaces the whole class with a fake function
    """

    def fake_coloring(color):
        return 'fake color!'

    with mock.patch('garage.Garage', fake_coloring):
        garage.Garage('test')
