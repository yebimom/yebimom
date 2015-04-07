from __future__ import absolute_import

from rest_framework.generics import ListAPIView

from centers.models import RegionThirdLayer
from api.serializers.regions import RegionSerializer


class RegionList(ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        search_query = self.request.GET.get("search", None)
        if search_query is not None:
            return RegionThirdLayer.objects.filter(name__contains=search_query)

        return RegionThirdLayer.objects.all()
