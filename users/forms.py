from django.forms import ModelForm
from users.models.contact import Question


class ContactForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['user']
