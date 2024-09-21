import unittest
from app import app, db
from users.models import User
from users.services import UserService

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def create_user_success(self):
        response = self.app.post('/users/', json={'name': 'Test User', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test User', response.get_data(as_text=True))

    def create_user_missing_fields(self):
        response = self.app.post('/users/', json={'name': 'Test User'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name and email are required', response.get_data(as_text=True))

    def create_user_invalid_email(self):
        response = self.app.post('/users/', json={'name': 'Test User', 'email': 'invalid-email'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', response.get_data(as_text=True))

    def create_user_email_in_use(self):
        with app.app_context():
            UserService.create_user('Existing User', 'test@example.com')
        response = self.app.post('/users/', json={'name': 'Test User', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email already in use', response.get_data(as_text=True))

    def create_user_invalid_name_length(self):
        response = self.app.post('/users/', json={'name': 'Te', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name should be between 3 and 50 characters', response.get_data(as_text=True))

    def get_users_success(self):
        with app.app_context():
            UserService.create_user('Test User', 'test@example.com')
        response = self.app.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test User', response.get_data(as_text=True))

    def get_user_success(self):
        with app.app_context():
            user = UserService.create_user('Test User', 'test@example.com')
        response = self.app.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test User', response.get_data(as_text=True))

    def get_user_not_found(self):
        response = self.app.get('/users/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', response.get_data(as_text=True))

    def update_user_success(self):
        with app.app_context():
            user = UserService.create_user('Test User', 'test@example.com')
        response = self.app.put(f'/users/{user.id}', json={'name': 'Updated User', 'email': 'updated@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated User', response.get_data(as_text=True))

    def update_user_not_found(self):
        response = self.app.put('/users/999', json={'name': 'Updated User', 'email': 'updated@example.com'})
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', response.get_data(as_text=True))

    def delete_user_success(self):
        with app.app_context():
            user = UserService.create_user('Test User', 'test@example.com')
        response = self.app.delete(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('User deleted', response.get_data(as_text=True))

    def delete_user_not_found(self):
        response = self.app.delete('/users/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()