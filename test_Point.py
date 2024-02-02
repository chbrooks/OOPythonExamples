from unittest import TestCase
from Point import *

class Test(TestCase):
    def test_point(self):
        p = Point(2, 2)
        p2 = Point(1, 1)
        print(p2 - p)
