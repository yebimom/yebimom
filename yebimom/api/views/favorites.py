from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView

from rest_framework.permissions import IsAuthenticated

from users.models import Favorite
from centers.models import Center

from api.serializers.favorites import FavoriteSerializer


class CreateFavorite(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    model = Favorite
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            center=Center.objects.get(hash_id=self.kwargs['hash_id']),
        )


class UserFavoritesList(ListAPIView):
    model = Favorite
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
