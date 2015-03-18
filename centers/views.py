# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Form
from centers.forms import CenterForm

# Model
from centers.models.center import Center


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
        'centers/center_register.html',
        {'center_form': center_form}
    )


def center(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        centers = Center.objects.filter(name__icontains=query)
        return render(request, 'centers/center_list.html',
                      {'centers': centers, 'query': query}
                      )
    else:
        return HttpResponse("검색을 클릭해주세요.")


def center_register_complete(request):
    return HttpResponse("Center Registration COMPLETE!")
