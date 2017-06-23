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
