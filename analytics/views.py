from django.shortcuts import render
from .models import CampaignAnalytics

def show_analytics(request):
    analytics_data = CampaignAnalytics.objects.all()
    return render(request, 'analytics/analytics_list.html', {'analytics_data': analytics_data})
