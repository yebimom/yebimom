from django.shortcuts import redirect

from django.contrib.auth.views import login as default_login_view
from django.contrib.auth import logout


def login_view(request):
    return default_login_view(
        request, template_name="users/login.html"
    )


def logout_view(request):
    logout(request)
    return redirect("home")
