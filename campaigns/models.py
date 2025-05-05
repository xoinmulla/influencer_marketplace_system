from django.db import models
from accounts.models import Profile
class Campaign(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    # Use a string reference instead of importing Profile directly
    brand = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='campaigns')
    influencers = models.ManyToManyField('accounts.Profile', blank=True, related_name='influencer_campaigns')

    def __str__(self):
        return self.title
