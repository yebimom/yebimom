from __future__ import absolute_import

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from reviews.models import VisitReview as Review
# from reviews.models import UseReview

from api.serializers.reviews import ReviewSerializer
from centers.models.center import Center
from users.models.user import UserProfile

import json


class UserReviewList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class CreateReview(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    model = Review
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        username = request.user.username
        center_hash_id = self.kwargs['hash_id']

        center_object = Center.objects.get(hash_id=center_hash_id)
        user_object = UserProfile.objects.get(user__username=username)

        payload = json.loads(request.body)

        review_object = Review()
        review_object.user = user_object.user
        review_object.center = center_object
        review_object.content = payload['content']
        review_object.save()

        # self.perform_create()
        # headers = self.get_success_headers()
        return Response(status=status.HTTP_201_CREATED)


# TODO-wonkyun: Need Documentation
class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    model = Review
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, *args, **kwargs):
        username = request.user.username
        center_hash_id = self.kwargs['hash_id']

        payload = json.loads(request.body)

        review_object = Review.objects.get(center__hash_id=center_hash_id,
                                           user__username=username)
        review_object.content = payload['content']
        review_object.save()

        return Response(status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        username = request.user.username
        center_hash_id = self.kwargs['hash_id']

        review_object = Review.objects.get(center__hash_id=center_hash_id,
                                           user__username=username)
        review_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)