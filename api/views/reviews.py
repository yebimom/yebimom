from __future__ import absolute_import

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from reviews.models import VisitReview as Review

from api.serializers.reviews import ReviewSerializer
from centers.models.center import Center
from users.models.user import UserProfile


class UserReviewList(ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class CreateReview(CreateAPIView):
    permission_classes = (IsAuthenticated, )

    model = Review
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        center = Center.objects.get(hash_id=kwargs['hash_id'])

        review = Review.objects.create(
            user=user,
            center=center,
            content='hello world',
        )

        return Response(status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyReview(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    model = Review
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.model.objects.get(center__hash_id=self.kwargs['hash_id'])
