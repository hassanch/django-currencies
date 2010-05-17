from django.contrib import admin

from currencies.models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol', 'factor', 'is_default',
                    'is_active')
    list_display_links = ('code', 'name', 'symbol')

admin.site.register(Currency, CurrencyAdmin)
