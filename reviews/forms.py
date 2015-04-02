from django import forms

from reviews.models import VisitReview as Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('user', 'center', )
