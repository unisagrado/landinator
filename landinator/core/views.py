from datetime import date
from landinator.core.services import save_subscription
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url as r
from landinator.core.forms import SubscriptionForm
from landinator.landing_pages.models import LandingPage


def home(request, slug=''):
    landing = get_object_or_404(LandingPage, slug=slug)
    if request.method == 'POST':
        return create(request, landing)
    return empty_form(request, landing)


def empty_form(request, landing):
    context = {'landing': landing, 'form': SubscriptionForm()}
    return render(request, 'index.html', context)


def create(request, landing):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        context = {'landing': landing, 'form': form}
        return render(request, 'index.html', context)

    save_subscription(form.cleaned_data, landing)
    return HttpResponseRedirect(r('success'))


def success(request):
    return render(request, 'subscription/success.html')
