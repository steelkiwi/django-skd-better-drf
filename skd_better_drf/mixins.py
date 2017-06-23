from django.db import models
from django.contrib.gis.db.models import PointField as PointFieldModel


from rest_framework.fields import (
    BooleanField, CharField, ChoiceField, DateField, DateTimeField,
    DecimalField, DictField, DurationField, EmailField, Field, FileField,
    FilePathField, FloatField, HiddenField, IPAddressField, ImageField,
    IntegerField, JSONField, ListField, ModelField, MultipleChoiceField,
    NullBooleanField, ReadOnlyField, RegexField, SerializerMethodField,
    SlugField, TimeField, URLField, UUIDField,
)


from skd_better_drf.fields import PointField


class FixFiledMixin:
    serializer_field_mapping = {
        models.AutoField: IntegerField,
        models.BigIntegerField: IntegerField,
        models.BooleanField: BooleanField,
        models.CharField: CharField,
        models.CommaSeparatedIntegerField: CharField,
        models.DateField: DateField,
        models.DateTimeField: DateTimeField,
        models.DecimalField: DecimalField,
        models.EmailField: EmailField,
        models.Field: ModelField,
        models.FileField: FileField,
        models.FloatField: FloatField,
        models.ImageField: ImageField,
        models.IntegerField: IntegerField,
        models.NullBooleanField: NullBooleanField,
        models.PositiveIntegerField: IntegerField,
        models.PositiveSmallIntegerField: IntegerField,
        models.SlugField: SlugField,
        models.SmallIntegerField: IntegerField,
        models.TextField: CharField,
        models.TimeField: TimeField,
        models.URLField: URLField,
        models.GenericIPAddressField: IPAddressField,
        models.FilePathField: FilePathField,
        PointFieldModel: PointField,
    }

    def __init__(self, *args, **kwargs):
        """Helper for Pycharm syntax checker"""
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        obj = super().to_representation(value)
        for key in obj:
            if obj[key] == '':
                obj[key] = None
        return obj
