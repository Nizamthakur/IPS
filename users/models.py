from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile (models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE )
    image = models.ImageField(default = 'profilepic.jpg', upload_to ='Profile_pictures')
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
