from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.urls import reverse

from .models import Weight


class WeightTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.weight = Weight.objects.create(
            datestamp='2012-12-12',
            weight=60.50,
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_weight_content(self):
        """ for content. """
        self.assertEqual(self.weight.id, 1)
        self.assertEqual(self.weight.datestamp, '2012-12-12')
        self.assertEqual(self.weight.weight, 60.50)
        self.assertEqual(self.weight.author, self.user)

    def test_weight_listview(self):
        """ for listview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('weight-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 60.50)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('weight-index')), 'weights/index.html')
        self.assertTemplateUsed(self.client.get(reverse('add-weight')), 'weights/add.html')
        self.assertTemplateUsed(self.client.get(reverse('update-weight', args='1')), 'weights/update.html')
        self.assertTemplateUsed(self.client.get(reverse('delete-weight', args='1')), 'weights/delete.html')
