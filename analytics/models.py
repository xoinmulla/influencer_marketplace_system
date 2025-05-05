from django.db import models
from campaigns.models import Campaign

class CampaignAnalytics(models.Model):
    campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    impressions = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    conversions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Analytics for {self.campaign.title}"
