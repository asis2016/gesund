from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.urls import reverse


class LeaderboardTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_leaderboards_templateview(self):
        """ for templateview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('leaderboards-index'))
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('leaderboards-index')), 'leaderboards/index.html')
