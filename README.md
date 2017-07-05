## Simple library for DRF
#### How to use:
##### Better time
Specify this parameters in your REST_FRAMEWORK settings.py:

`'DATETIME_FORMAT': '%d.%m.%Y %H:%M:%S %z'`,

`'DATETIME_INPUT_FORMATS': ['%d.%m.%Y %H:%M:%S %z']`,

`'DATE_FORMAT': '%d.%m.%Y'`,

`'DATE_INPUT_FORMATS': ['%d.%m.%Y']`,

`'TIME_FORMAT': '%H:%M:%S'`,

`'TIME_INPUT_FORMATS': ['%H:%M:%S']`.

##### FixFiledMixin
###### models.py
```python
class City(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    location = PointField(verbose_name=_('location'), null=True, blank=True)

    def __str__(self):
        return self.name
```
###### serializers.py
```python
class CitySerializer(FixFiledMixin, serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'location', )
```

Response example:
```javascript
{
    "id": 2,
    "name": "Kiev",
    "location": {
        "latitude": 50.448427,
        "longitude": 30.529860
    }
}
```
##### NonePagination
###### views.py
```python
class CityModelViewSet(ModelViewSet):
    serializer_class = CitySerializer
    pagination_class = NonePagination

    def get_queryset(self):
        return City.objects.all()
```
###### urls.py
```python
urlpatterns = [
    url(r'^city/$', CityModelViewSet.as_view({'get': 'list'}), name='city'),
]
```
Response example:
```javascript
{
    "results": [
        {
            "id": 2,
            "name": "Kiev",
            "location": {
                "latitude": 50.448427,
                "longitude": 30.529860
            }
        }
     ]

}
```
##### Swagger doc
You would specify `responses_docs` in view using dict. Read more about [json schema](https://swagger.io/specification/).
Also you can use `parameters_docs` in view for parameters.

`skd_better_drf.swagger.base_responses` contains base responses and response for NonePagination.

```python
       responses_docs = {
        'get': {
            '200': {
                'description': 'Success! Instance successfully received',
                'schema': {
                    "title": "Person",
                    "type": "object",
                    "properties": {
                        "firstName": {
                            "type": "string",
                            "example": "My first name"
                        },
                        "lastName": {
                            "type": "string",
                            "example": "My last name"
                        },
                        "age": {
                            "description": "Age in years",
                            "type": "integer",
                            "minimum": 0,
                            "example": 16
                        }
                    },
                    "required": ["firstName", "lastName"]
                }
            },
        }
    }
```
###### urls.py
```python
urlpatterns = [
    url(r'^docs/$', SwaggerSchemaView.as_view()),
]
````
###### view.py
```python
from django.utils.translation import ugettext as _

from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_swagger import renderers

from skd_better_drf.swagger.schema import SchemaGenerator
from skd_better_drf.swagger.renderers import OpenAPIRenderer


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        CoreJSONRenderer,
        OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title=_('Doctor Raksa API'))
        schema = generator.get_schema(request=request)

        return Response(schema)
```