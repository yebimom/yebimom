from django.views.generic import View, TemplateView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from centers.models.center import Center
from centers.models.center_landing import CenterLanding

from centers.forms import CenterLandingForm
from django.core.urlresolvers import reverse


class ManagementBaseView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManagementBaseView, self).dispatch(*args, **kwargs)


class ManagementDashboard(ManagementBaseView, TemplateView):
    template_name = "managements/home.html"


class ManagementCenterBase(ManagementBaseView, DetailView):
    model = Center
    context_object_name = "center"

    def get_object(self):
        return Center.objects.get(hash_id=self.kwargs['hash_id'])


class ManagementCenterDashboard(ManagementCenterBase):
    template_name = "managements/center.html"


class ManagementCenterLanding(ManagementCenterBase, FormView):
    template_name = "managements/landing.html"
    form_class = CenterLandingForm

    def get_context_data(self, **kwargs):
        context = super(ManagementCenterLanding, self).get_context_data(**kwargs)
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])
        context['center_landings'] = center.centerlanding_set.all()

        return context

    def form_valid(self, form):
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])

        self.object = form.save(commit=False)
        self.object.center = center

        self.object.save()

        return super(ManagementCenterLanding, self).form_valid(self)

    def get_success_url(self):
        center = Center.objects.get(hash_id=self.kwargs['hash_id'])
        return reverse("managements:landing-list", kwargs={'hash_id': center.hash_id})
