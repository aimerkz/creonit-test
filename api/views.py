from django_filters import rest_framework as filters

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.filters import UrlModelFilter
from api.models import UrlModel
from api.serializers import UrlModelSerializer


class ListUrlView(ListAPIView):

    serializer_class = UrlModelSerializer
    queryset = UrlModel.objects.all()
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UrlModelFilter

    def get_queryset(self):
        return self.filter_queryset(self.queryset).first()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
