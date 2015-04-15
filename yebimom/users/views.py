from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.views import login as default_login_view

from django.views.generic.detail import DetailView

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Decorators
from django.utils.decorators import method_decorator
from users.decorators import anonymous_required
from django.contrib.auth.decorators import login_required

# Forms
from users.forms import ContactForm
from django.contrib.auth.forms import UserCreationForm


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
            login(request, user)

            return redirect("home")

        return render(request, "users/signup.html", {
            'form': user_form
        })

    return render(request, "users/signup.html", {
        'form': UserCreationForm
    })


@login_required
def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form = contact_form.save(commit=False)
            contact_form.user = request.user
            contact_form.save()

    return render(request, "users/contact.html", {
        'form': ContactForm
    })


class UserBase(DetailView):
    context_object_name = 'user'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserBase, self).dispatch(*args, **kwargs)

    def get_object(self):
        return self.request.user


class Dashboard(UserBase):
    template_name = "users/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['favorites'] = self.request.user.userprofile.favorites.all()[:3]
        return context


class Favorites(UserBase):
    template_name = "users/favorites.html"

    def get_context_data(self, **kwargs):
        context = super(Favorites, self).get_context_data(**kwargs)
        context['favorites'] = self.request.user.userprofile.favorites.all()
        return context
