import wdbd.hi as hi
import unittest


class TestHi(unittest.TestCase):

    def test_hi(self):
        hi.hello()


if __name__ == "__main__":
    hi.hello()
