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
            # 1 - GRADUAÇÃO
            if subscription.landing_page.to == '1':
                client = LaharClient(settings.LAHAR_GRADUATION_TOKEN, event=landing.slug)
                token_api = settings.LAHAR_GRADUATION_TOKEN

            # 2 - PÓS-GRADUAÇÃO
            elif subscription.landing_page.to == '2':
                client = LaharClient(settings.LAHAR_POSTGRADUATE_TOKEN, event=landing.slug)
                token_api = settings.LAHAR_POSTGRADUATE_TOKEN

            integration_data = dict(
                email_contato=subscription.email,
                nome_contato=subscription.first_name,
                sobrenome=subscription.last_name,
                tel_celular=subscription.celphone,
                tel_fixo=subscription.phone,
                tags=landing.tag,
                token_api_lahar=token_api,
                nome_formulario=subscription.landing_page.title,
            )

            client.create_lead(integration_data)
        except Exception as err:
            print(err)
            return
