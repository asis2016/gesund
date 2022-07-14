from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class DashboardTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.client.login(username='testuser', password='secret')
        self.assertTemplateUsed(self.client.get(reverse('dashboard')), 'dashboard/index.html')
