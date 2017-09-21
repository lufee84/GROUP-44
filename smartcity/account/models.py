from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return super(UserProfileManager, self).get_queryset().filter(type='Admin')


class UserProfile(models.Model):
    STUDENT = 1
    TOURIST = 2
    BUSINESS = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TOURIST, 'Tourist'),
        (BUSINESS, 'Business'),
        (ADMIN, 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    # admin = UserProfileManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
