from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, permissions
from blogpost.models import Blogpost
from rest_framework.response import Response

class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Blogpost
        fields = {'title','author', 'body', 'slug'}

class BlogpostSet(viewsets.ModelViewSet):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly)

    def list(self, request):
        queryset = Blogpost.objects.all()
        search_param = self.request.query_params.get('title', None)
        if search_param:
            queryset = Blogpost.objects, filter(title__contains = search_param)
        serializers = BlogpostSerializer(queryset, many=True)
        return Response(serializers.data)
