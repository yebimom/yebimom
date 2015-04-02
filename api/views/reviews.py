from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Rest-Framework Jwt
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from reviews.models import VisitReview as Review
from reviews.models import UseReview

from api.serializers.review_serializer import ReviewSerializer
from centers.models.center import Center


class UserAllReviewList(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        username = request.user.username
        review = Review.objects.filter(user__username=username)
        serializer = ReviewSerializer(review, many=True)

        return Response(serializer.data)
