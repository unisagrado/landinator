from landinator.core.models import Subscription


def save_subscription(form, landing):
    subscription = Subscription(**form.cleaned_data)
    subscription.landing_page = landing
    subscription.save()
