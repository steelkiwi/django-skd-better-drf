## Simple library for DRF
#### How to use:
##### FixFiledMixin
Миксин реализует замену `PointField` и  пустых строк на объект `null`. 
Поскольку поле может содержать атрибут `null=True` значения могут возвращаться как `'''` или `null`, что приводит
к некоторым трудностям при разработке приложений под мобильные платформы с использованием статически типизированых 
языков програмирования.
`PointField` возвращает человекочитаемое отображения координат (смотрите ниже). Исключает путаницу с значениями 
`latitude` и `longitude`.
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
`NonePagination` позволяет отключить пагинацию не нарушив работу существующего кода на фронт-энде, также 
При использовании `pagination_class = None` в ответ приходит массив без ключа, что создает проблемы при обработке
с использованием статически типизированых языков.
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
