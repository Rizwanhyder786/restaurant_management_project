from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
class UserProfileTestCase(TestCase):
    def setUp(self):
        #create a sample user and user profile
        self.user = user.objects.create_user(username='testuser',password='testpass')
        self.profile = UserProfile.objects.create(
            user=self.user,
            phone='1234567890',
            address='Hyderabad,India',
            date_of_birth='2002-01-01'
        )
        def test_profile_created(self):
            #tesr if the profile is linked to the correct user
            self.assertEqual(self.profile.user.username.'testuser')
            self.assertEqual(self.profile.phone,'1234567890')