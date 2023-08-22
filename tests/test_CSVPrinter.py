import unittest
from unittest import TestCase

from speciallecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def test_something(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        print(l)
        self.assertEqual("value2B", l[1][1])  # add assertion here

    def test_read3(self):
        try:
            printer = CSVPrinter("sample1.csv")
            printer.read()
            self.fail("a")
        except FileNotFoundError as e:
            pass