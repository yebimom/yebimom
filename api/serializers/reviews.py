from __future__ import absolute_import

from rest_framework import serializers

from reviews.models import VisitReview as Review
from reviews.models import UseReview

from users.models.user import User
from centers.models.center import Center


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('user', 'center')
