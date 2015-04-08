from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

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


class ReviewBase(APIView):
    permission_classes = (IsAuthenticated, )

    model = Review
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            center=Center.objects.get(hash_id=self.kwargs['hash_id']),
        )

    def get_object(self):
        return Review.objects.get(
            user=self.request.user,
            center=Center.objects.get(hash_id=self.kwargs['hash_id']),
        )


class CreateReview(ReviewBase, CreateAPIView):
    pass


class UpdateReview(ReviewBase, UpdateAPIView):
    pass


class DestroyReview(ReviewBase, DestroyAPIView):
    pass
