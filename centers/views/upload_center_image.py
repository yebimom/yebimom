from django.shortcuts import render
from centers.forms.center_image_form import CenterImageForm
from centers.utils.handle_upload_file import handle_uploaded_file


def upload(request):
    form = CenterImageForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            handle_uploaded_file(request.FILES['image'])
            return render(request, "home.html")

    return render(request, "centers/upload.html", {'form': form})
