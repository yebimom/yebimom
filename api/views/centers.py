from __future__ import absolute_import

from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from centers.models import Center
from centers.serializers import CenterSerializer


class CenterList(ListAPIView):
    serializer_class = CenterSerializer

    def get_queryset(self):
        search_query = self.request.GET.get('term', None)
        if search_query is not None:
            return Center.objects.filter(name__contains=search_query)

        return Center.objects.all()


class CenterDetail(RetrieveAPIView):

    lookup_field = 'hash_id'
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
