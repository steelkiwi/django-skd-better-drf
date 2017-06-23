## Simple library for DRF
#### How to use:
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
```python
class CityModelViewSet(ModelViewSet):
    serializer_class = CitySerializer
    pagination_class = NonePagination

    def get_queryset(self):
        return City.objects.all()
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
