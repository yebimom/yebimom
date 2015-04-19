from __future__ import absolute_import

from rest_framework.generics import ListAPIView

from centers.models import Category
from centers.models import Center

from api.serializers.categories import CategorySerializer
from api.serializers.centers import CenterSerializer


class CategoryList(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetail(ListAPIView):
    serializer_class = CenterSerializer

    def get_queryset(self):
        return Category.objects.get(slug=self.kwargs['slug']).centers.all()
