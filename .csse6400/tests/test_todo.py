import unittest
from todo import create_app

TEST_TODO = {
            "id": 1,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00"
        }


class TestTodo(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_get_todo(self):
        response = self.client.get('/api/v1/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [TEST_TODO])

    def test_get_todo_by_id(self):
        response = self.client.get('/api/v1/todos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, TEST_TODO)

    def test_post_todo(self):
        response = self.client.post('/api/v1/todos', json=TEST_TODO)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, TEST_TODO)

    def test_put_todo(self):
        response = self.client.put('/api/v1/todos/1', json=TEST_TODO)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, TEST_TODO)

    def test_delete_todo(self):
        response = self.client.delete('/api/v1/todos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, TEST_TODO)

