from django import forms

from reviews.models import VisitReview


class VisitReviewForm(forms.ModelForm):

    class Meta:
        model = VisitReview
        exclude = ('user', 'center', )
