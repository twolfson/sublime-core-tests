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

class TestSublimeErrorMessage(unittest.TestCase):
    def test_sublime_error_message(self):
        """
        A sublime package
            has a method for `error_message`
        """
        # DEV: We cannot fully test `error_message` as it generates a UI dialog
        self.assertEquals(hasattr(sublime, 'error_message'), True)

class TestSublimeMessageDialog(unittest.TestCase):
    def test_sublime_message_dialog(self):
        """
        A sublime package
            has a method for `message_dialog`
        """
        # DEV: We cannot fully test `message_dialog` as it generates a UI dialog
        self.assertEquals(hasattr(sublime, 'message_dialog'), True)

class TestSublimeOkCancelDialog(unittest.TestCase):
    def test_sublime_ok_cancel_dialog(self):
        """
        A sublime package
            has a method for `ok_cancel_dialog`
        """
        # DEV: We cannot fully test `ok_cancel_dialog` as it generates a UI dialog
        self.assertEquals(hasattr(sublime, 'ok_cancel_dialog'), True)

class TestSublimeYesNoCancelDialog(unittest.TestCase):
    def test_sublime_yes_no_cancel_dialog(self):
        """
        A sublime package
            has a method for `yes_no_cancel_dialog`
        """
        # DEV: We cannot fully test `yes_no_cancel_dialog` as it generates a UI dialog
        self.assertEquals(hasattr(sublime, 'yes_no_cancel_dialog'), True)

class TestSublimeVersion(unittest.TestCase):
    def test_sublime_version(self):
        """
        A sublime package
            supplies a valid version
        """
        version = sublime.version()
        # e.g. 3114
        self.assertRegexpMatches(version, r'3\d{3}')
