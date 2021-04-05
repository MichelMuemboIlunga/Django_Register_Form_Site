from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    sex = models.CharField(
        max_length=1,
        choices=gender,
    )
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username