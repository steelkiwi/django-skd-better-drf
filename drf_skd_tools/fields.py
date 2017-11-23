import json

from datetime import datetime
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos.error import GEOSException
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

EMPTY_VALUES = (None, '', [], (), {})


class PointField(serializers.Field):
    """
    From https://github.com/Hipo/drf-extra-fields
    A field for handling GeoDjango Point fields as a json format.
    Expected input format:
        {
        "latitude": 49.8782482189424,
         "longitude": 24.452545489
        }
    """
    type_name = 'PointField'
    type_label = 'point'

    default_error_messages = {
        'invalid': _('Enter a valid location.'),
    }

    def to_internal_value(self, value):
        """
        Parse json data and return a point object
        """
        if value in EMPTY_VALUES and not self.required:
            return None

        if isinstance(value, six.string_types):
            try:
                value = value.replace("'", '"')
                value = json.loads(value)
            except ValueError:
                self.fail('invalid')

        if value and isinstance(value, dict):
            try:
                latitude = value.get("latitude")
                longitude = value.get("longitude")
                return GEOSGeometry('POINT(%(longitude)s %(latitude)s)' % {
                    "longitude": longitude,
                    "latitude": latitude}
                                    )
            except (GEOSException, ValueError):
                self.fail('invalid')
        self.fail('invalid')

    def to_representation(self, value):
        """
        Transform POINT object to json.
        """
        if value is None:
            return value

        if isinstance(value, GEOSGeometry):
            value = {
                "latitude": value.y,
                "longitude": value.x
            }
        return value


class TimestampField(serializers.Field):
    default_error_messages = {
        'invalid': _('Should be an integer.'),
    }

    def to_internal_value(self, value):
        if value in EMPTY_VALUES and not self.required:
            return None

        try:
            int_value = int(value)
        except ValueError:
            self.fail('invalid')
        return datetime.fromtimestamp(int_value)

    def to_representation(self, value):
        if value is None:
            return value

        assert isinstance(value, datetime), 'Expected a `datetime`'

        return int(value.timestamp())
