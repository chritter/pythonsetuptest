import bisect
import unittest

class SortedList(list):
    """
    original class to test

    Args:
        list ([type]): [description]
    """
    def __init__(self, iterable):
        super(SortedList, self).__init__(sorted(iterable))

    def insort(self, item):
        bisect.insort(self, item)


    def extend(self, other):
        for item in other:
            self.insort(item)

    @staticmethod
    def append(o):
        raise RuntimeError("Cannot append to a sorted list")

    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop], value)
        if start:
            place += start
        end = stop or len(self)
        if place < end and self[place] == value:
            return place
        raise ValueError("%s is not in list" % value)


class TestSortedList(unittest.TestCase):
    """
    Testing class

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        # we initialize the class with fixed values
        self.mylist = SortedList(['a', 'c', 'd', 'x', 'f', 'g', 'w'])

    def test_sorted_init(self):
        # here we even test the proper initailization of the class
        self.assertEqual(sorted(['a', 'c', 'd', 'x', 'f', 'g', 'w']),
            self.mylist)

    def test_sorted_insort(self):
        # test first class function, note multipe tests per function, good?
        self.mylist.insort('z')
        self.assertEqual(['a', 'c', 'd', 'f', 'g', 'w', 'x', 'z'],
            self.mylist)
        self.mylist.insort('b')
        self.assertEqual(['a', 'b', 'c', 'd', 'f', 'g', 'w', 'x', 'z'],
            self.mylist)

    def test_index(self):
        self.assertEqual(0, self.mylist.index('a'))
        self.assertEqual(1, self.mylist.index('c'))
        self.assertEqual(5, self.mylist.index('w'))
        self.assertEqual(0, self.mylist.index('a', stop=0))
        self.assertEqual(0, self.mylist.index('a', stop=2))
        self.assertEqual(0, self.mylist.index('a', stop=20))
        self.assertRaises(ValueError, self.mylist.index, 'w', stop=3)
        self.assertRaises(ValueError, self.mylist.index, 'a', start=3)
        self.assertRaises(ValueError, self.mylist.index, 'a', start=333)

    def test_extend(self):
        # call class to execute function
        self.mylist.extend(['b', 'h', 'j', 'c'])
        # then test function
        self.assertEqual(['a', 'b', 'c', 'c', 'd', 'f', 'g', 'h', 'j',
            'w', 'x'], self.mylist)