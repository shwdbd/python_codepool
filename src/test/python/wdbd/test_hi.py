import wdbd.codepool.hi as hello
import unittest


class TestHi(unittest.TestCase):

    def test_hi(self):
        hello.hello()


if __name__ == "__main__":
    hello.hello()
