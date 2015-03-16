from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.views import login as default_login_view
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Decorators
from users.decorators import anonymous_required


@anonymous_required
def login_view(request):
    return default_login_view(
        request, template_name="users/login.html"
    )


def logout_view(request):
    logout(request)
    return redirect("home")


@anonymous_required
def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()

            user = authenticate(username=username, password=password)
            user_profile = user.userprofile

            login(request, user)
            return redirect("home")

        return render(request, "users/signup.html", {
            'form': user_form
        })

    return render(request, "users/signup.html", {
        'form': UserCreationForm
    })
