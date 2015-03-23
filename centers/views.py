# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Form
from centers.forms import CenterForm
from reviews.forms import ReviewForm

# Model
from centers.models.center import Center
from reviews.models import Review

# Decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def center_register(request):
    if request.method == 'GET':
        center_form = CenterForm()
    else:
        center_form = CenterForm(request.POST)

        if center_form.is_valid():
            center_form.save()
            return HttpResponseRedirect(reverse('centers:register_complete'))

    return render(
        request,
        'centers/register.html',
        {'center_form': center_form}
    )


def center_register_complete(request):
    return HttpResponse("Center Registration COMPLETE!")


class CenterList(ListView):
    template_name = 'centers/list.html'
    context_object_name = 'centers'

    def get_queryset(self):
        search_query = self.request.GET.get('search') or str()
        return Center.objects.filter(name__contains=search_query)


class CenterDetail(DetailView):
    model = Center
    template_name = 'centers/detail.html'
    context_object_name = 'center'
    slug_field = 'hash_id'

    def get_context_data(self, **kwargs):
        context = super(CenterDetail, self).get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context


@login_required
@require_http_methods(["POST"])
def reviews(request, slug):
    user = request.user
    center = Center.objects.get(hash_id=slug)

    review = Review.objects.create(
        user=user,
        center=center,
        content=request.POST['content'],
    )

    return redirect("centers:detail", slug=slug)
