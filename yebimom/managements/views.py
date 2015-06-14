from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from centers.models.center import Center


class ManagementBaseView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManagementBaseView, self).dispatch(*args, **kwargs)


class ManagementDashboard(ManagementBaseView, TemplateView):
    template_name = "managements/home.html"


class ManagementCenterLanding(ManagementBaseView, ListView):
    template_name = "managements/landing.html"
    context_object_name = "center_landings"

    def get_queryset(self):
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])
        return center.centerlanding_set.all()

    def get_context_data(self, **kwargs):
        context = super(ManagementCenterLanding, self).get_context_data(**kwargs)
        context['center'] = Center.objects.get(hash_id=self.kwargs['hash_id'])
        return context
