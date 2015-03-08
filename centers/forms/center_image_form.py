from centers.models.image import CenterImage
from django.forms import ModelForm


class CenterImageForm(ModelForm):
    class Meta:
        model = CenterImage
        fields = ['image']
