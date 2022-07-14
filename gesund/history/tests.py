from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import History


class HistoryTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.history = History.objects.create(
            app='steps',
            action='CREATE',
            description='10000 STEPS WERE ADDED!',
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_history_content(self):
        """ for content. """
        # 1 won't work because signals are in used.
        # self.assertEqual(self.history.id, 1)
        # auto_now_add argument provided in model
        # self.assertEqual(self.history.datestamp, '2012-12-12')
        self.assertEqual(self.history.app, 'steps')
        self.assertEqual(self.history.action, 'CREATE')
        self.assertEqual(self.history.author, self.user)
        self.assertEqual(self.history.description, '10000 STEPS WERE ADDED!')

    def test_history_templateview(self):
        """ for templateview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('history-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ADDED!')

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('history-index')), 'history/index.html')
