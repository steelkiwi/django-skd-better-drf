from collections import OrderedDict
from rest_framework.pagination import BasePagination
from rest_framework.response import Response


class NonePagination(BasePagination):
    """Remove pagination, use when you no need pagination"""

    def paginate_queryset(self, queryset, request, view=None):
        return queryset

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('results', data)
        ]))