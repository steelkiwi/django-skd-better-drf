import json

import coreapi
from coreapi.compat import force_bytes
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework_swagger.renderers import OpenAPIRenderer, OpenAPICodec
from rest_framework_swagger.settings import swagger_settings

from skd_better_drf.swagger.encode import AbstractCodec


class OpenAPICodec(AbstractCodec, OpenAPICodec):
    def encode(self, document, extra=None, **options):
        if not isinstance(document, coreapi.Document):
            raise TypeError('Expected a `coreapi.Document` instance')

        data = self._generate_swagger_object(document)
        if isinstance(extra, dict):
            data.update(extra)

        return force_bytes(json.dumps(data))


class OpenAPIRenderer(OpenAPIRenderer):
    media_type = 'application/openapi+json'
    charset = None
    format = 'openapi'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context['response'].status_code != status.HTTP_200_OK:
            return JSONRenderer().render(data)
        extra = self.get_customizations()

        return OpenAPICodec().encode(data, extra=extra)

    def get_customizations(self):
        """
        Adds settings, overrides, etc. to the specification.
        """
        data = {}
        if swagger_settings.SECURITY_DEFINITIONS:
            data['securityDefinitions'] = swagger_settings.SECURITY_DEFINITIONS

        return data