from django.test import TestCase
from django.contrib.auth.models import User
from .models import Entry

class EntryTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()

        # # Create and save a new page to the test database.
        # new_entry = Entry(title="My Test Page", content="test", author=user)
        # new_entry = Entry(entry_title="My Test Page", entry_text="test",entry-date='' ,entry_author=user)
        # new_entry.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(new_entry.slug, "my-test-page")
