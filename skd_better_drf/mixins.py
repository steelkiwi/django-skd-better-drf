from rest_framework.fields import (
    BooleanField, CharField, ChoiceField, DateField, DateTimeField,
    DecimalField, DictField, DurationField, EmailField, Field, FileField,
    FilePathField, FloatField, HiddenField, IPAddressField, ImageField,
    IntegerField, JSONField, ListField, ModelField, MultipleChoiceField,
    NullBooleanField, ReadOnlyField, RegexField, SerializerMethodField,
    SlugField, TimeField, URLField, UUIDField,
)


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
        models.FileField: FileFieldWithoutNone,
        models.FloatField: FloatField,
        models.ImageField: ImageFieldWithoutNone,
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
    }