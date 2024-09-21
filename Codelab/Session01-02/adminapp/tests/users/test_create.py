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
