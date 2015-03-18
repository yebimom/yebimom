from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from centers.models import Center
from centers.serializers import CenterSerializer


class CenterList(ListAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer


class CenterDetail(RetrieveAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
