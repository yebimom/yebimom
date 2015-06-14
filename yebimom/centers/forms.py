from django.forms import ModelForm
from centers.models.center_landing import CenterLanding


class CenterLandingForm(ModelForm):

    class Meta:
        model = CenterLanding
        fields = ['title', ]
