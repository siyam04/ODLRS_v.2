from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name_plural = 'Customer Profiles'

    def __str__(self):
        return self.user.username


