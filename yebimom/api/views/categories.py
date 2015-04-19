from __future__ import absolute_import

from rest_framework.generics import ListAPIView

from centers.models import Category
from centers.models import Center

from api.serializers.categories import CategorySerializer


class CategoryList(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
