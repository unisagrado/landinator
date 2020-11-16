from django.shortcuts import render
from landinator.core.forms import SubscriptionForm


def home(request):
    form = SubscriptionForm()
    return render(request, 'index.html', {'form': form})
