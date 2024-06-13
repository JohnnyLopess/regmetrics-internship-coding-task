import unittest
from unittest import TestCase


def foo(x=0, y=[]):
    y.append(x)
    return "Even" if len(y) % 2 == 0 else "Odd"


class TestFoo(TestCase):
    def test_foo__empty(self):
        self.assertEqual(foo(), "Odd")

    def test_foo__1(self):
        self.assertEqual(foo(1), "Odd")

    def test_foo__2(self):
        self.assertEqual(foo(2), "Odd")

    def test_foo__1_empty(self):
        self.assertEqual(foo(1, []), "Odd")

    def test_foo__1_123(self):
        self.assertEqual(foo(1, [1, 2, 3]), "Even")


if __name__ == "__main__":
    unittest.main()
