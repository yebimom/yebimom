from django import forms

from reviews.models import VisitReview
from reviews.models import UseReview


class VisitReviewForm(forms.ModelForm):

    class Meta:
        model = VisitReview
        exclude = ('user', 'center', )


class UseReviewForm(forms.ModelForm):

    class Meta:
        model = UseReview
        exclude = ('user', 'center', )
