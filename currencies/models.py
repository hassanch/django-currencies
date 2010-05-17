from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=1)
    factor = models.DecimalField(max_digits=10, decimal_places=6,
        help_text=_('Specifies the difference of the currency to default one.'))
    is_active = models.BooleanField(default=True,
        help_text=_('The currency will be available.'))
    is_default = models.BooleanField(default=False,
        help_text=_('Make this the default currency.'))

    class Meta:
        verbose_name_plural = _('Currencies')

    def __unicode__(self):
        return self.code

    def save(self, **kwargs):
        """Sets all is_default currencies to not default if this is default."""
        if self.is_default:
            defaults = Currency.objects.filter(is_default=True)
            if self.pk:
                defaults = defaults.exclude(pk=self.pk)
            for currency in defaults:
                currency.is_default = False
                currency.save()
        super(Currency, self).save(**kwargs)
