# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


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


def map(request, latitude, longitude, width, height):
    return render(request, "map.html", {
        "latitude": latitude,
        "longitude": longitude,
        "width": width,
        "height": height,
    })
