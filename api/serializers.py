from rest_framework import serializers

from api.models import UrlModel


class UrlModelSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = UrlModel
        fields = ('name', 'url', 'children')

    def get_children(self, obj):
        children = obj.get_descendants()
        serializer = UrlModelSerializer(children, many=True)
        return serializer.data
