from django.test import TestCase
# from django.contrib.auth.models import User
from unittest.mock import patch
from user.models import CustomUser


class UserSignalTest(TestCase):
    """Mock the send_mail function directly: This is the simplest way to test signals."""
    @patch('user.signals.send_mail')  # Mock the send_mail function
    def test_send_welcome_email(self, mock_send_mail):
        # Create a user to trigger the signal
        user = CustomUser.objects.create_user(first_name="testuser", email="1322noobmaster@gmail.com", password="password123")

        # Check that send_mail was called with correct arguments
        mock_send_mail.assert_called_once_with(
            subject="Welcome to Our Platform",
            message=f"Hi {user.first_name} {user.last_name}, welcome to our platform!",
            from_email="ramandhiman1322@gmail.com",
            recipient_list=["1322noobmaster@gmail.com"],
            fail_silently=False,
        )


class UserSignalTest2(TestCase):
    """Mock the Celery task's .delay method:"""
    @patch('user.tasks.send_welcome_email_task.delay')  # Mock the Celery task's delay method
    def test_send_welcome_email_task(self, mock_celery_task):
        # Create a user to trigger the signal
        user = CustomUser.objects.create_user(first_name="testuser", email="1322noobmaster@gmail.com", password="password123")

        # Check that the Celery task was called with correct arguments
        mock_celery_task.assert_called_once_with(user.first_name, user.email)
