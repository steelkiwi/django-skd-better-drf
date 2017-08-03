import uuid

from django.utils.translation import ugettext as _

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class MobileTokenAuthentication(BaseAuthentication):
    KEYWORD = 'Token'
    model = None

    def get_headers_values(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split()
        device_id = request.META.get('HTTP_DEVICE_ID', '')
        return token, device_id

    def authenticate(self, request):
        token, device_id = self.get_headers_values(request)

        if len(token) < 2:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(token) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        token_keyword = token[0]
        token_value = token[1]

        if not token_keyword or token_keyword.lower() != self.KEYWORD.lower():
            return None

        if not device_id:
            return None

        try:
            uuid.UUID(device_id)
        except ValueError:  # catch badly formed hexadecimal UUID string
            msg = _('Invalid device id. Id should be a uuid.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token_value, device_id)

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token

    def authenticate_credentials(self, token, device_id):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=token)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.devices.filter(device_id=device_id).exists():
            raise exceptions.AuthenticationFailed(_('Invalid device'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return token.user, token

