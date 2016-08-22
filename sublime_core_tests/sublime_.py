# Load in our dependencies
# DEV: We can't name this file `sublime.py` otherwise we get issues with UnitTesting
import sublime
import unittest

# Define our tests
class TestSublimeSetTimeout(unittest.TestCase):
    def test_sublime_set_timeout(self):
        """
        A sublime package
            has a method for `set_timeout`
        """
        # TODO: Test set_timeout call itself
        self.assertEquals(hasattr(sublime, 'set_timeout'), True)

class TestSublimeSetAsyncTimeout(unittest.TestCase):
    # TODO: Figure out why we cannot find `set_async_timeout`
    @unittest.skip('`set_async_timeout` doesn\'t seem to exist in Sublime Text 3114')
    def test_sublime_set_async_timeout(self):
        """
        A sublime package
            has a method for `set_async_timeout`
        """
        # TODO: Test set_async_timeout call itself
        self.assertEquals(hasattr(sublime, 'set_async_timeout'), True)

class TestSublimeVersion(unittest.TestCase):
    def test_sublime_version(self):
        """
        A sublime package
            supplies a valid version
        """
        version = sublime.version()
        # e.g. 3114
        self.assertRegexpMatches(version, r'3\d{3}')
