from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import WaterIntake


class WaterIntakeTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.water_intake = WaterIntake.objects.create(
            datestamp='2012-12-12',
            drink_progress=2.5,
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_waterintake_content(self):
        """ for content. """
        self.user_loggedin_instance()
        self.assertEqual(self.water_intake.id, 1)
        self.assertEqual(self.water_intake.drink_progress, 2.5)
        self.assertEqual(self.water_intake.author, self.user)

    def test_waterintake_listview(self):
        """ for listview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('water-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 2.5)

    def test_templates_used(self):
        """ check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('water-index')), 'water_intake/index.html')
        self.assertTemplateUsed(self.client.get(reverse('add-water-progress')), 'water_intake/add.html')
        self.assertTemplateUsed(self.client.get(reverse('update-water-progress', args='1')), 'water_intake/update.html')
        self.assertTemplateUsed(self.client.get(reverse('delete-water-progress', args='1')), 'water_intake/delete.html')
