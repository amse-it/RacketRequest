from django.test import TestCase
from django.utils import timezone
from .models import Request, Racket
from user_profile.models import UserProfile
import datetime


class RequestTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserProfile.objects.create(username='user', password='1234')

    def test_has_expired_with_an_old_request(self):
        """
        `has_expired()` should return `True` for a request that is older than
        it's duration.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        r = Request(
            title='Test Request',
            description='Make me a car',
            duration=10,
            created=time,  # r is not saved so created is not replaced
            owner=self.user,
        )

        self.assertTrue(r.has_expired())

    def test_has_expired_with_a_recent_request(self):
        """
        `has_expired()` should return `False` for a request that is younger
        than it's duration.
        """
        r = Request(
            title='Test Request',
            description='Make me a song',
            duration=10,
            owner=self.user,
        )
        r.save()
        self.assertFalse(r.has_expired())


def create_racket(request, owner, date_started):
    return Racket.objects.create(
        request=request,
        owner=owner,
        title='test racket',
        description='test desc',
        date_started=date_started,
    )


class RacketTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.requester = UserProfile.objects.create(
            username='requester', password='1234')
        cls.racket_owner = UserProfile.objects.create(
            username='racket_owner', password='1234')
        cls.request = Request.objects.create(
            title='req', description='desc', duration=10, owner=cls.requester)

    def test_has_started_with_past_date_started(self):
        """
        `has_started` should return True if `date_started` yesterday.
        """
        r = create_racket(self.request, self.racket_owner,
                          timezone.now() - datetime.timedelta(days=1))
        self.assertTrue(r.has_started())

    def test_has_started_with_future_date_started(self):
        """
        `has_started` should return False if `date_started` tomorrow.
        """
        r = create_racket(self.request, self.racket_owner,
                          timezone.now() + datetime.timedelta(days=1))
        self.assertFalse(r.has_started())
