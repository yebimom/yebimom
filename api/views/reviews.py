from __future__ import absolute_import

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from reviews.models import VisitReview as Review
from reviews.models import UseReview

from api.serializers.reviews import ReviewSerializer
from centers.models.center import Center


class UserReviewList(ListAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
