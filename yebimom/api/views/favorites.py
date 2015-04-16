from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from centers.models import Center
from api.serializers.centers import CenterSerializer


class FavoriteBase(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CenterSerializer

    def get_queryset(self):
        return self.request.user.userprofile.favorites.all()

    def post(self, request, *args, **kwargs):
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])
        self.request.user.userprofile.favorites.add(center)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])
        self.request.user.userprofile.favorites.remove(center)

        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateFavorite(FavoriteBase):
    pass


class DeleteFavorite(FavoriteBase):
    pass


class UserFavoritesList(FavoriteBase, ListAPIView):
    pass
