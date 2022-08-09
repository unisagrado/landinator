from django.db import models


class Subscription(models.Model):
    first_name = models.CharField('primeiro nome', max_length=50)
    last_name = models.CharField('sobrenome', max_length=50)
    email = models.EmailField('e-mail')
    celphone = models.CharField('celular', max_length=20)
    phone = models.CharField('telefone', max_length=20, blank=True, null=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    privacity_policy = models.BooleanField('aceita_política?', default=False)
    send_offers = models.BooleanField('aceita_envio?', default=False)
    landing_page = models.ForeignKey(
        'landing_pages.LandingPage', verbose_name='formulário', on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
