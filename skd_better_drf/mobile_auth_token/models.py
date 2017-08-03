from django.db import models
from django.utils.translation import ugettext as _

from rest_framework.authtoken.models import Token


class Device(models.Model):
    device_id = models.UUIDField(_('device id'))
    created = models.DateTimeField(_('created at'), auto_now_add=True)
    modified = models.DateTimeField(_('modified at'), auto_now=True)
    token = models.ForeignKey(Token,  related_name='devices', on_delete=models.CASCADE, verbose_name=_('Device'))

    class Meta:
        abstract = True
        verbose_name = _('Token')
        verbose_name_plural = _('Tokens')

