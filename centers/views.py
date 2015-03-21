# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods

# Views
from django.views.generic.detail import DetailView

# Form
from centers.forms import CenterForm

# Model
from centers.models.center import Center


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


@require_http_methods(["GET", "POST"])
def center(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        centers = Center.objects.filter(name__icontains=query)
        return render(request, 'centers/list.html', {'centers': centers, 'query': query})
    else:
        centers = Center.objects.all()
        return render(request, 'centers/list.html', {'centers': centers})


def center_register_complete(request):
    return HttpResponse("Center Registration COMPLETE!")


class CenterDetail(DetailView):
    model = Center
    template_name = 'centers/detail.html'
    context_object_name = 'center'
    slug_field = 'hash_id'
