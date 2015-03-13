from django.shortcuts import render
from django.http import HttpResponse


def center_registration(request):
    if request.method == 'GET':
        return render(request, 'centers/center_registration.html')
    else:
        errors = []
        try:
            name = request.POST.get('name', 0)
            address = request.POST.get('address', 0)
            phone = request.POST.get('phone', 0)
            url = request.POST.get('url', 0)
            price = request.POST.get('price', 0)
            result = name, address, phone, url, price
        except ValueError:
            errors.append('Not a Valid Value')
            result = 0

        return render(
            request,
            'centers/center_registration.html',
            {'result': result, 'errors': errors}
        )


def center(request):
    return HttpResponse("Center")
