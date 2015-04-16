from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.permissions import IsAuthenticated

from centers.models import Center
from api.serializers.centers import CenterSerializer


class FavoriteBase(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CenterSerializer

    def get_queryset(self):
        return self.request.user.userprofile.favorites.all()


class CreateFavorite(FavoriteBase, CreateAPIView):
    pass


class UserFavoritesList(FavoriteBase, ListAPIView):
    pass
