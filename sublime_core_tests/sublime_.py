# Load in our dependencies
# DEV: We can't name this file `sublime.py` otherwise we get issues with UnitTesting
import sublime
from unittest import TestCase

# Define our tests
# TODO: Collect untested methods
class TestSublimeVersion(TestCase):
    def test_sublime_version(self):
        """
        A sublime package
            supplies a valid version
        """
        version = sublime.version()
        # e.g. 3114
        self.assertRegexpMatches(version, r'3\d{3}')
