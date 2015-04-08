from __future__ import absolute_import

from rest_framework import serializers

from reviews.models import VisitReview
from reviews.models import UseReview

from users.models.user import User
from centers.models.center import Center


class VisitReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitReview
        exclude = ('user', 'center')


class UseReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = UseReview
        exclude = ('user', 'center')
