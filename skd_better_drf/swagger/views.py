from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_swagger import renderers

from skd_better_drf.swagger.schema import SchemaGenerator
from skd_better_drf.swagger.renderers import OpenAPIRenderer


def get_swagger_view(title=None, url=None, patterns=None, urlconf=None):
    class SwaggerSchemaView(APIView):
        permission_classes = [AllowAny]
        renderer_classes = [
            CoreJSONRenderer,
            OpenAPIRenderer,
            renderers.SwaggerUIRenderer
        ]

        def get(self, request):
            generator = SchemaGenerator(title=title, url=url, patterns=patterns, urlconf=urlconf)
            schema = generator.get_schema(request=request)

            return Response(schema)

    return SwaggerSchemaView.as_view()