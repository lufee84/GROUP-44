from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

options = [
    ('0', 'Student'),
    ('1', 'Tourist'),
    ('2', 'Business'),
    ('3', 'Admin'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=options)

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
