from django.test import TestCase
from django.utils import timezone
from .models import Request
from user_profile.models import UserProfile
import datetime


class RequestTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserProfile.objects.create(username='user', password='1234')

    def test_is_expired_with_an_old_request(self):
        """
        `is_expired` should return `True` for a request that is older than it's
        duration.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        r = Request(
            title='Test Request',
            description='Make me a car',
            duration=10,
            created=time,  # r is not saved so created is not replaced
            owner=self.user,
        )

        self.assertTrue(r.is_expired)

    def test_is_expired_with_a_recent_request(self):
        """
        `is_expired` should return `False` for a request that is younger than
        it's duration.
        """
        r = Request(
            title='Test Request',
            description='Make me a song',
            duration=10,
            owner=self.user,
        )
        r.save()
        self.assertFalse(r.is_expired)
