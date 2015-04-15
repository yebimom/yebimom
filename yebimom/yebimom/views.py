# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.shortcuts import render

from centers.models import Center


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        """
        this is just a simple example for centers/templates/centers/list/_centers.html
        should refactor after Category app is finished.
        """
        context['centers_with_celeb'] = Center.objects.all()[:3]
        context['centers_with_window_view'] = Center.objects.all()[:3]
        return context


def service(request):
    """
    이용약관
    """
    return render(request, "rules/service.html", {})


def privacy(request):
    """
    개인정보 취급방침
    """
    return render(request, "rules/privacy.html", {})


def disclaimer(request):
    """
    책임의 한계와 법적고지
    """
    return render(request, "rules/disclaimer.html", {})


def search_policy(request):
    """
    검색결과 수집에 대한 정책
    """
    return render(request, "rules/search_policy.html", {})
