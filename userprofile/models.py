from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')

    phone = models.CharField(max_length=20,blank=True)

    portrait = ProcessedImageField(
        upload_to='portrait/%Y%m%d',
        processors=[ResizeToFit(width=400,height=400)],
        options={'quality':100},
    )

    bio = models.TextField(max_length=600, blank=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)


