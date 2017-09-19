from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

options = [
    ('Student', 'Student'),
    ('Tourist', 'Tourist'),
    ('Business', 'Business'),
    ('Admin', 'Admin'),
]


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(type='Admin')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    type = models.CharField(max_length=8, choices=options)

    admin = UserProfileManager()

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
