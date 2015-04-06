from __future__ import absolute_import

from rest_framework.generics import ListAPIView

from centers.models import RegionThirdLayer
from api.serializers.regions import RegionSerializer


class RegionList(ListAPIView):
    queryset = RegionThirdLayer.objects.all()
    serializer_class = RegionSerializer
