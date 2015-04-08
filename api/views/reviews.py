from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from reviews.models import VisitReview
from reviews.models import UseReview

from api.serializers.reviews import VisitReviewSerializer
from api.serializers.reviews import UseReviewSerializer

from centers.models.center import Center
from users.models.user import UserProfile


class UserReviewList(ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = VisitReviewSerializer

    def get_queryset(self):
        return VisitReview.objects.filter(user=self.request.user)


class ReviewBase(APIView):
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            center=Center.objects.get(hash_id=self.kwargs['hash_id']),
        )

    def get_object(self):
        return self.model.objects.get(
            user=self.request.user,
            center=Center.objects.get(hash_id=self.kwargs['hash_id']),
        )


class VisitReviewBase(ReviewBase):
    model = VisitReview
    serializer_class = VisitReviewSerializer


class UseReviewBase(ReviewBase):
    model = UseReview
    serializer_class = UseReviewSerializer


class CreateVisitReview(VisitReviewBase, CreateAPIView):
    pass


class UpdateVisitReview(VisitReviewBase, UpdateAPIView):
    pass


class DeleteVisitReview(VisitReviewBase, DestroyAPIView):
    pass


class CreateUseReview(UseReviewBase, CreateAPIView):
    pass


class UpdateUseReview(UseReviewBase, UpdateAPIView):
    pass


class DeleteUseReview(UseReviewBase, DestroyAPIView):
    pass
