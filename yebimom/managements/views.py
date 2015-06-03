from django.views.generic import View, TemplateView


class Home(TemplateView):
    template_name = "managements/home.html"
