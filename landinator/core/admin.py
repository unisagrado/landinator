from landinator.core.mixins import ExportMixin
from django.contrib import admin
from landinator.core.models import Subscription
from django.shortcuts import resolve_url as r
from django.utils.html import format_html


class SubscriptionModelAdmin(admin.ModelAdmin, ExportMixin):
    list_display = ('__str__', 'landing_page', 'email', 'celphone',
                    'page_link', 'privacity_policy', 'send_offers', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('landing_page__title',
                     'landing_page__slug', 'first_name', 'last_name')
    list_filter = ('landing_page__title', 'landing_page__slug')
    actions = ['export_as_csv', 'export_xlsx']

    def page_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', r('home', obj.landing_page.slug))

    page_link.short_description = 'link'


admin.site.register(Subscription, SubscriptionModelAdmin)
