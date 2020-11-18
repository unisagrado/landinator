from landinator.core.models import Subscription


def save_subscription(data, landing):
    subscription = Subscription(**data)
    subscription.landing_page = landing
    if landing.enabled():
        subscription.save()
    return subscription
