from django_filters import rest_framework as filters

from api.models import UrlModel


class UrlModelFilter(filters.FilterSet):
    url = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = UrlModel
        fields = ['url']
