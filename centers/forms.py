from django import forms
from django.utils.translation import ugettext_lazy as _

# Model
from centers.models.center import Center


class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ['region_third_layer', 'name', 'address', 'phone', 'url', 'price']
        # exclude = ('region_first_layer', 'region_second_layer')
        labels = {
            'region_third_layer': _('Region'),
            'name': _('Center Name'),
            'address': _('Address'),
            'phone': _('Phone'),
            'url': _('Homepage URL'),
            'price': _('Price(per 2weeks)'),
        }
        error_massages = {
            'name': {
                'max_length': _("This Center's name is too long.")
            },
        }
        localized_fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if '-' in phone:
            raise forms.ValidationError("You have to enter phone number without Hypen(-)")
        elif len(phone) > 11:
            raise forms.ValidationError("You have to enter 11or10-digit phone number")

        return phone