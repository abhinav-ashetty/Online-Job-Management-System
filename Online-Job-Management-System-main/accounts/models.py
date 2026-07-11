from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


# class User(AbstractUser):
#     username = None
#     role = models.CharField(max_length=12, error_messages={
#         'required': "Role must be provided"
#     })
#     gender = models.CharField(max_length=10, blank=True, null=True, default="")
#     email = models.EmailField(unique=True, blank=False,
#                               error_messages={
#                                   'unique': "A user with that email already exists.",
#                               })

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     def __unicode__(self):
#         return self.email

#     objects = UserManager()

class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False, error_messages={
        'unique': "A user with that email already exists.",
    })

    # Add your new fields here
    phone = models.CharField(max_length=15, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

