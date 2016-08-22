# Load in our dependencies
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
        # Retrieve and assert our version
        version = sublime.version()
        self.assertEqual(version, 2000)
