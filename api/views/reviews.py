from __future__ import absolute_import

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from reviews.models import VisitReview as Review
# from reviews.models import UseReview

from api.serializers.reviews import ReviewSerializer


class UserReviewList(ListAPIView):
    permission_classes = (IsAuthenticated, )

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class CreateReview(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (JSONWebTokenAuthentication, )

    model = Review
    serializer_class = ReviewSerializer

    def get_object(self):
        return self.model.objects.get(center__hash_id=self.kwargs['hash_id'],
                                      user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     username = request.user.username

    # def forms_valid(self, form, inlines):
    #     form.instance.owner = self.request.user
    #     return super(CreateReview, self).forms_valid(form, inlines)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )

    model = Review
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.model.objects.get(center__hash_id=self.kwargs['hash_id'])
