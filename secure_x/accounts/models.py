from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custom manager where email is the unique identifier for authentication."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom User model that uses email instead of username."""
    username = None  # Remove the username field
    email = models.EmailField('email address', unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('business', 'Business Owner'),
        ('institution', 'Institution'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')

    USERNAME_FIELD = 'email'  # Login with email
    REQUIRED_FIELDS = []  # No extra required fields

    objects = CustomUserManager()

    def __str__(self):
        return self.email
