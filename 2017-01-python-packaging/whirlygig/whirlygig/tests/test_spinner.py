import unittest

from whirlygig.spinner import Spinner


class TestSpinner(unittest.TestCase):

    def test_spinning_is_fun(self):
        spinner = Spinner()
        self.assertEqual('Weee!', spinner.spin())
