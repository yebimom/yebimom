from __future__ import absolute_import

from rest_framework import serializers

from reviews.models import VisitReview as Review
from reviews.models import UseReview

from users.models.user import User
from centers.models.center import Center


class ReviewSerializer(serializers.ModelSerializer):
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False,)
    center = serializers.PrimaryKeyRelatedField(queryset=Center.objects.all(), required=False)

    class Meta:
        model = Review
        fields = ('content', )
        exclude = ('user', 'center')
