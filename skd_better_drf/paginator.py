from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class NonePagination(PageNumberPagination):
    """Remove pagination, but response will be with get_paginated_response()"""
    def paginate_queryset(self, queryset, request, view=None):
        return queryset

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('results', data)
        ]))