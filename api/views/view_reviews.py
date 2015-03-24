# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from centers.models.center import Center
from reviews.models import Review
from users.models.user_profile import UserProfile


class UserAllReviewList(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):

        username = request.user.username

        # 일단 하나만 가져오도록 해봄.
        review = Review.objects.get(user__username=username)

        data = {
            'id': request.user.id,
            'username': username,
            'center': review.center.name,
            'review': review.content,
        }

        return Response(data)
