from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from django.urls import reverse

from .models import Pomodoro


class PomodoroTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.pomodoro = Pomodoro.objects.create(
            pomodoro=1,
            short_break=1,
            long_break=1,
            remarks='good work!',
            author=self.user
        )

    def user_loggedin_instance(self):
        """ for user login. """
        return self.client.login(username='testuser', password='secret')

    def test_pomodoro_content(self):
        """ for content. """
        self.assertEqual(self.pomodoro.id, 1)
        self.assertEqual(self.pomodoro.pomodoro, 1)
        self.assertEqual(self.pomodoro.short_break, 1)
        self.assertEqual(self.pomodoro.remarks, 'good work!')
        self.assertEqual(self.pomodoro.author, self.user)

    def test_pomodoro_listview(self):
        """ for listview. """
        self.user_loggedin_instance()
        response = self.client.get(reverse('pomodoro-index'))
        self.assertEqual(response.status_code, 200)

    def test_templates_used(self):
        """ Check if templates are correct. """
        self.user_loggedin_instance()
        self.assertTemplateUsed(self.client.get(reverse('pomodoro-index')), 'pomodoros/index.html')
        self.assertTemplateUsed(self.client.get(reverse('add-pomodoro')), 'pomodoros/add.html')
        self.assertTemplateUsed(self.client.get(reverse('detail-pomodoro', args='1')), 'pomodoros/detail.html')
        self.assertTemplateUsed(self.client.get(reverse('pomodoro-datestamp-collection', args=['2012-12-12'])),
                                'pomodoros/list_by_date.html')
