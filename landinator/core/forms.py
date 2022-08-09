from django import forms


class SubscriptionForm(forms.Form):
    first_name = forms.CharField(label='Primeiro nome*')
    last_name = forms.CharField(label='Sobrenome*')
    email = forms.EmailField(label='E-mail*')
    celphone = forms.CharField(label='Celular*')
    phone = forms.CharField(label='Telefone', required=False)
    privacity_policy = forms.BooleanField(required=False)
    send_offers = forms.BooleanField(required=False)

    first_name.widget.attrs.update({'placeholder': first_name.label})
    last_name.widget.attrs.update({'placeholder': last_name.label})
    email.widget.attrs.update({'placeholder': email.label})
    celphone.widget.attrs.update({'placeholder': celphone.label})
    phone.widget.attrs.update({'placeholder': phone.label})
    privacity_policy.widget.attrs.update({'required': False})
    send_offers.widget.attrs.update({'required': False})
