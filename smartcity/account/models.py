from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return super(UserProfileManager, self).get_queryset().filter(type='Admin')


class UserProfile(models.Model):

    business = 'Business'
    student = 'Student'
    tourist = 'Tourist'
    admin = 'ADMIN'

    ROLE_CHOICES = (
        (business, 'Business'),
        (student, 'Student'),
        (tourist, 'Tourist'),
        (admin, 'ADMIN')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    role = models.CharField(
        max_length=8,
        choices=ROLE_CHOICES,
        default=business,
        )

    # admin = UserProfileManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
