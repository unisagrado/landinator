from landinator.core.models import Subscription
from django.conf import settings
from lahar import Client as LaharClient


def save_subscription(data, landing):
    subscription = Subscription(**data)
    subscription.landing_page = landing
    if landing.enabled():
        subscription.save()

    integrate_mailmarketing(subscription)

    return subscription


def integrate_mailmarketing(subscription):
    landing = subscription.landing_page

    if landing.should_integrate() and subscription.pk is not None and settings.LAHAR_TOKEN:
        try:
            client = LaharClient(settings.LAHAR_TOKEN,
                                 event=landing.slug)

            integration_data = dict(
                email_contato=subscription.email,
                nome_contato=subscription.first_name,
                sobrenome=subscription.last_name,
                tel_celular=subscription.celphone,
                tel_fixo=subscription.phone,
                tags=landing.tag,
            )

            client.create_lead(integration_data)
        except Exception as err:
            print(err)
            return
