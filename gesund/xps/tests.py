from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.urls import reverse

from .models import XP


class XPModelTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.xp = XP.objects.create(
            xp=1,
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_xps_templateview(self):
        """ for templateview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('xps-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 1000)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('xps-index')), 'xps/index.html')
