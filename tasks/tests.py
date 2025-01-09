from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import SimpleTask
from rest_framework import status


class TestTask(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='test')
        self.user2 = User.objects.create_user(username='user2', password='test')
        
        task1 = SimpleTask.objects.create(user=self.user1, title='task1', completed=False)
        task2 = SimpleTask.objects.create(user=self.user2, title='task2', completed=True)

        self.task1_id = task1.id
        self.task2_id = task2.id

    def test_user1_login(self):
        self.client.login(username='user1', password='test')
        response = self.client.get('/api/tasks/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user1_task(self):
        self.client.login(username='user1', password='test')
        response = self.client.post('/api/tasks/', {'title': 'task1', 'completed': False})
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_only_get_own_task(self):
        self.client.login(username='user1', password='test')
        response1 = self.client.get(f'/api/task/{self.task1_id}/', follow=False)
        response2 = self.client.get(f'/api/task/{self.task2_id}/', follow=False)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_only_update_own_task(self):
        self.client.login(username='user1', password='test')
        response1 = self.client.patch(f'/api/task/{self.task1_id}/', {'completed': True}, follow=False,
                                      content_type='application/json')
        response2 = self.client.patch(f'/api/task/{self.task2_id}/', {'completed': True}, follow=False,
                                      content_type='application/json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_only_delete_own_task(self):
        self.client.login(username='user1', password='test')
        response1 = self.client.delete(f'/api/task/{self.task1_id}/', follow=False)
        response2 = self.client.delete(f'/api/task/{self.task2_id}/', follow=False)
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)