from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.
class TestTasks(APITestCase):
    task_url = '/api/v1/tasks/'
    fixtures = ['users', 'tasks']

    def setUp(self) -> None:
        super().setUp()
        auth_response = self.client.post('/api/token/', { 'username': 'test_user', 'password': '12345678' })
        token = auth_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_return_user_tasks(self):
        user = User.objects.get(id=1)
        response = self.client.get(self.task_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Task.objects.filter(user=user).count())

    def test_create_user_task(self):
        old_task_count = Task.objects.count()
        response = self.client.post(self.task_url, data={ 'title': 'Exercise.' })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(old_task_count <= Task.objects.count(), True)

    def test_return_first_user_task(self):
        user = User.objects.get(id=1)
        first_task = Task.objects.filter(user=user).first()
        response = self.client.get(f'{self.task_url}{first_task.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), first_task.title)

    def test_update_user_task(self):
        user = User.objects.get(id=1)
        first_task = Task.objects.filter(user=user).first()
        task_payload = { 'title': 'Update', 'done': True }
        response = self.client.put(f'{self.task_url}{first_task.pk}/', data=task_payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_task = Task.objects.filter(user=user).first()
        self.assertEqual(updated_task.title, 'Update')
        self.assertEqual(updated_task.done, True)

    def test_delete_user_task(self):
        user = User.objects.get(id=1)
        old_task_count = Task.objects.filter(user=user).count()
        first_task = Task.objects.filter(user=user).first()
        response = self.client.delete(f'{self.task_url}{first_task.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), old_task_count - 1)
