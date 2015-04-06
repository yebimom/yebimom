from __future__ import absolute_import

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from reviews.models import VisitReview as Review
from reviews.models import UseReview

from api.serializers.reviews import ReviewSerializer


class UserReviewList(ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
