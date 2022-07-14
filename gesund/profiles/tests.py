from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.urls import reverse

from .models import Profile


class ProfileTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.profile = Profile.objects.create(
            name='John Doe',
            dob='2012-12-12',
            gender='M',
            height=170,
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_profile_content(self):
        """ for content """
        # self.assertEqual(self.profile.id, 1)
        self.assertEqual(self.profile.name, 'John Doe')
        self.assertEqual(self.profile.dob, '2012-12-12')
        self.assertEqual(self.profile.gender, 'M')
        self.assertEqual(self.profile.height, 170)
        self.assertEqual(self.profile.author, self.user)

    def test_profile_templateview(self):
        """ for templateView. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('profile-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('profile-index')), 'profiles/index.html')
        self.assertTemplateUsed(self.client.get(reverse('update-profile', args='1')), 'profiles/update.html')
