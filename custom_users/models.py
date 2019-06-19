from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    profile_name = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Customer Profiles'

    def __str__(self):
        return self.user.username


