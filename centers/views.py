from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Form
from centers.forms import CenterForm


def center_register(request):
    if request.method == 'GET':
        center_form = CenterForm()
    else:
        center_form = CenterForm(request.POST)

        if center_form.is_valid():
            center_form.save()
            return HttpResponseRedirect('/center/register_complete')

    return render(
        request,
        'centers/center_register.html',
        {'center_form': center_form}
    )


def center(request):
    return HttpResponse("Center")


def center_register_complete(request):
    return HttpResponse("Center Registration COMPLETE!")
