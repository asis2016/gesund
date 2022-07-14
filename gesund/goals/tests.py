from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Goals


class GoalsTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.goals = Goals.objects.create(
            calories=2500,
            steps=8000,
            water=3.1,
            weight=65.5,
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_goals_content(self):
        """ for content """
        # self.assertEqual(self.goals.id, 1)
        self.assertEqual(self.goals.calories, 2500)
        self.assertEqual(self.goals.steps, 8000)
        self.assertEqual(self.goals.water, 3.1)
        self.assertEqual(self.goals.weight, 65.5)
        self.assertEqual(self.goals.author, self.user)

    def test_goals_templateview(self):
        """ for templateview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('goals-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 8000)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('goals-index')), 'goals/index.html')
        self.assertTemplateUsed(self.client.get(reverse('update-goals', args='1')), 'goals/update.html')
