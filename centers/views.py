from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import HttpResponseRedirect

from centers.models.center import Center
from centers.models.facility import Facility
from centers.models.policy import Policy
from centers.models.region import RegionSecondLayer
from centers.models.region import RegionThirdLayer
from reviews.models import VisitReview
from reviews.models import UseReview

from reviews.forms import VisitReviewForm
from reviews.forms import UseReviewForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST

from django.conf import settings


class CenterList(ListView):
    template_name = 'centers/list.html'
    context_object_name = 'centers'

    def get_queryset(self):
        search_query = self.request.GET.get('search') or str()
        location_query = self.request.GET.get('location') or str()
        if location_query is not '':
            regions_second_layer = RegionSecondLayer.objects.filter(name__contains=location_query)
            regions_third_layer = RegionThirdLayer.objects.filter(name__contains=location_query)
            centers_region_second_layer = Center.objects.filter(region_second_layer__contains=regions_second_layer)
            centers_region_third_layer = Center.objects.filter(region_third_layer__contains=regions_third_layer)
            return centers_region_second_layer | centers_region_third_layer
        return Center.objects.filter(name__contains=search_query)


class CenterDetail(DetailView):
    model = Center
    template_name = 'centers/detail.html'
    context_object_name = 'center'
    slug_field = 'hash_id'

    def get_context_data(self, **kwargs):
        context = super(CenterDetail, self).get_context_data(**kwargs)
        context['visit_review_form'] = VisitReviewForm()
        context['use_review_form'] = UseReviewForm()
        context['facilities'] = Facility.objects.all()
        context['policies'] = Policy.objects.all()
        context['NAVER_OPENAPI_MAP_API_KEY'] = getattr(settings, 'NAVER_OPENAPI_MAP_API_KEY', False)
        return context


class VisitReviewBase(View):
    model = VisitReview
    fields = ['content', ]

    @method_decorator(require_POST)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VisitReviewBase, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse("centers:detail", kwargs=self.kwargs)

    def get_object(self):
        return VisitReview.objects.get(center__hash_id=self.kwargs['slug'], user=self.request.user)


class VisitReviewCreate(VisitReviewBase, CreateView):
    def form_valid(self, form):
        review = form.save(commit=False)
        review.center = Center.objects.get(hash_id=self.kwargs['slug'])
        review.user = self.request.user
        review.save()
        return HttpResponseRedirect(self.get_success_url())


class VisitReviewUpdate(VisitReviewBase, UpdateView):
    pass


class VisitReviewDelete(VisitReviewBase, DeleteView):
    pass


class UseReviewBase(View):
    model = UseReview
    fields = ['content', ]

    @method_decorator(require_POST)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UseReviewBase, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse("centers:detail", kwargs=self.kwargs)

    def get_object(self):
        return UseReview.objects.get(center__hash_id=self.kwargs['slug'], user=self.request.user)


class UseReviewCreate(UseReviewBase, CreateView):
    def form_valid(self, form):
        review = form.save(commit=False)
        review.center = Center.objects.get(hash_id=self.kwargs['slug'])
        review.user = self.request.user
        review.save()
        return HttpResponseRedirect(self.get_success_url())


class UseReviewUpdate(UseReviewBase, UpdateView):
    pass


class UseReviewDelete(UseReviewBase, DeleteView):
    pass
