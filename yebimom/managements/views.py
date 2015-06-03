from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ManagementBaseView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManagementBaseView, self).dispatch(*args, **kwargs)


class ManagementDashboard(ManagementBaseView, TemplateView):
    template_name = "managements/home.html"


class ManagementCenterLanding(ManagementBaseView, TemplateView):
    template_name = "managements/landing.html"
