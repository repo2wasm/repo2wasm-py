import unittest

from .utils import clean_dependency


class TestCleanDependency(unittest.TestCase):
    def test_no_version(self):
        input = "numpy"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")

    def test_equality(self):
        input = "numpy=1.8.1"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")

    def test_exact_equality(self):
        input = "numpy==1.8.1"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")

    def test_greater(self):
        input = "numpy>1.8.1"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")

    def test_greater_or_equality(self):
        input = "numpy>=1.8.1"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")

    def test_less(self):
        input = "numpy<1.8.1"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")

    def test_less_or_equality(self):
        input = "numpy<=1.8.1"
        self.assertEqual(clean_dependency(input), input)
        self.assertEqual(clean_dependency(input, True), "numpy")
