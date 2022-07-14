from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Steps


class StepsTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.steps = Steps.objects.create(
            datestamp='2012-12-12',
            step_count=5000,
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_steps_content(self):
        """ for content. """
        self.assertEqual(self.steps.id, 1)
        self.assertEqual(self.steps.datestamp, '2012-12-12')
        self.assertEqual(self.steps.step_count, 5000)
        self.assertEqual(self.steps.author, self.user)

    def test_steps_listview(self):
        """ for listview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('steps-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 5000)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('steps-index')), 'steps/index.html')
        self.assertTemplateUsed(self.client.get(reverse('add-steps')), 'steps/add.html')
        self.assertTemplateUsed(self.client.get(reverse('update-steps', args='1')), 'steps/update.html')
        self.assertTemplateUsed(self.client.get(reverse('delete-steps', args='1')), 'steps/delete.html')
