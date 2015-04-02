from rest_framework import serializers

from reviews.models import VisitReview as Review
from reviews.models import UseReview


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
