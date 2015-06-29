from django.test import TestCase
from django.utils import timezone
from .models import Request
from user_profile.models import UserProfile
import datetime


class RequestTests(TestCase):
    user = UserProfile(username='user', password='123456')

    def setUp(self):
        self.user.save()

    def test_expiry_calculation(self):
        now = timezone.now()
        r = Request(
            title='Test Request',
            description='Make me a car',
            duration=10,
            created=now,
            owner=self.user
        )
        self.assertEqual(r.expiry - now, datetime.timedelta(days=10))

    def test_is_expired_with_an_old_request(self):
        time = timezone.now() - datetime.timedelta(days=30)
        r = Request(
            title='Test Request',
            description='Make me a car',
            duration=10,
            created=time,
            owner=self.user,
        )

        self.assertTrue(r.is_expired)
