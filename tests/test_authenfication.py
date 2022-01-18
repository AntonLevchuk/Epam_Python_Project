import unittest

from app import app


class User_testing(unittest.TestCase):
    """ Testing the registration, authentication """

    tester = app.test_client()

    def test_login_page(self, tester=tester):
        """ Ensure that the login page loads correctly """

        r = tester.post('/login', data=dict(email='insanelev@gmail.com', password='qwerty'))
        self.assertTrue(b'Logged in Successfully!', r.data)

    def test_logout(self, tester=tester):
        """ Ensure that the logout works correctly  """

        r = tester.post('/logout')
        self.assertTrue(b'You logged out!', r.data)

    def testing_registration(self, tester=tester):
        """ Ensure that the registration page loads correctly """

        r = tester.post('/register', data=dict(email='email@email.com', password='qwerty', username='test_user'))
        self.assertTrue(b'Thanks for registration!', r.data)
