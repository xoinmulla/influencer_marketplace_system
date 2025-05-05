# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('influencer', 'Influencer'),
        ('brand', 'Brand'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    # Optional: if you plan to use a profile image, add this field.

    def __str__(self):
        return f"{self.user.username} - {self.role}"
