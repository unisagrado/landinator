from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url as r
from landinator.core.forms import SubscriptionForm
from landinator.landing_pages.models import LandingPage


def home(request, slug=''):
    landing = get_object_or_404(LandingPage, slug=slug)
    if request.method == 'POST':
        return create(request, landing)
    return empty_form(request, landing)


def empty_form(request, landing):
    title = landing.title
    return render(request, 'index.html', {'title': title, 'form': SubscriptionForm()})


def create(request, landing):
    title = landing.title
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'index.html', {'title': title, 'form': form})

    return HttpResponseRedirect('sucesso/')


def success(request):
    return render(request, 'subscription/success.html')
