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

**You can use name of mapped functions by default
(`list`, `retrieve`, `create`, `update`, `partial_update`, `destroy`)
or map your own or standard `get`, `post`, `put`, `patch`, `delete`.**


`skd_better_drf.swagger.base_responses` contains base responses and response for NonePagination.

```python
       responses_docs = {
        "retrieve": {
            "200": {
                "description": "Success! Instance successfully received",
                "schema": {
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
        },
        "custom_list": {
            "200": {
                "type": "object",
                "description": "parse error",
                "schema": {
                    "properties": {
                        "filter_letter": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "description": "",
                                "example": "This field is required.",
                            }
                        }
                    }
                }
            }
        }
    }
```
###### urls.py
```python
from skd_better_drf.swagger.views import get_swagger_view

urlpatterns = [
    url(r'^docs/$', get_swagger_view(title='Pastebin API')),
]
````
##### Mobile token auth
Provides authentication backend and device model for authorization by token from mobile phones.
For using backend you should add class to setting and create model device from abstract Device model. 
###### settings.py
```python 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'skd_better_drf.mobile_auth_token.authentication.MobileTokenAuthentication',
    ),
}
```
###### models.py
```python
from skd_better_drf.mobile_auth_token.models import Device as BaseDevice
 
class Device(BaseDevice):
    pass
```
You can add additional fields and methods to your Device model.
Header name should be `Authorization` and `Device-id` for token and device id accordingly.  

Example:
```bash
http :8000/user/ Authorization:'Token 6df0cfb73a45353ab78cc69088fd32d392042b05' \
 Device-id:22bc4a64-783e-11e7-b5a5-be2e44b06b34
```