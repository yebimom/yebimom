from django.forms import ModelForm
from centers.models.center_landing import CenterLanding
from centers.models.center_contact import CenterContact


class CenterLandingForm(ModelForm):

    class Meta:
        model = CenterLanding
        fields = ['title', ]


class CenterContactForm(ModelForm):

    class Meta:
        model = CenterContact
        fields = ['name', 'phonenumber', 'description', ]
