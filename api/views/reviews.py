from __future__ import absolute_import
# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# rest framework JWT
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Review app
from reviews.models import Review
from api.serializers.review_serializer import ReviewSerializer

# Center app
from centers.models.center import Center


class UserAllReviewList(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        username = request.user.username
        review = Review.objects.filter(user__username=username)
        serializer = ReviewSerializer(review, many=True)

        return Response(serializer.data)
