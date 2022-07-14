from django.test import TransactionTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CalorieIntake


class CalorieIntakeTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.calorie_intake = CalorieIntake.objects.create(
            datestamp='2012-12-12',
            food='pasta',
            consume=400,
            description='test pasta',
            calories=1000,
            protein=500,
            fat=300,
            carb=200,
            sugar=0,
            fiber=0,
            author=self.user,
            food_detail_ref=1000
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_calorieintake_content(self):
        """ for content """
        self.assertEqual(self.calorie_intake.datestamp, '2012-12-12')
        self.assertEqual(self.calorie_intake.food, 'pasta')
        self.assertEqual(self.calorie_intake.description, 'test pasta')
        self.assertEqual(self.calorie_intake.calories, 1000)
        self.assertEqual(self.calorie_intake.protein, 500)
        self.assertEqual(self.calorie_intake.fat, 300)
        self.assertEqual(self.calorie_intake.carb, 200)
        self.assertEqual(self.calorie_intake.sugar, 0)
        self.assertEqual(self.calorie_intake.fiber, 0)
        self.assertEqual(self.calorie_intake.author, self.user)
        self.assertEqual(self.calorie_intake.food_detail_ref, 1000)

    def test_calorieintake_listview(self):
        """ for listview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('calorie-intake-datestamp-index'))
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('calorie-intake-datestamp-index')), 'calories/index.html')
        self.assertTemplateUsed(self.client.get(reverse('add-calorie-intake')), 'calories/add.html')
        self.assertTemplateUsed(self.client.get(reverse('update-calorie-intake', args='1')), 'calories/update.html')
        self.assertTemplateUsed(self.client.get(reverse('delete-calorie-intake', args='1')), 'calories/delete.html')
        self.assertTemplateUsed(
            self.client.get(reverse('calorie-intake-datestamp-collection-index', args=['2012-12-12'])),
            'calories/index-datestamp-collection.html')
