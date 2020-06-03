from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill 


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="uploads",default='default.png')
    profile_thumbnail = ImageSpecField(
                                 processors=[ResizeToFill(200, 200)],
                                 format='JPEG',
                                 options={'quality': 60})

    def __str__(self):
        return f'{self.user.username} profile'
