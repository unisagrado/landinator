from django.contrib import admin
from django.utils.html import format_html
from landinator.landing_pages.models import LandingPage


class LandingPageModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'tag', 'link', 'end_date']

    def link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.get_absolute_url())

    link.short_description = 'link'


admin.site.register(LandingPage, LandingPageModelAdmin)
