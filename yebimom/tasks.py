# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import shared_task

# Email
from django.core.mail import send_mail


@shared_task
def send_contact_us_email(email, title, content, phone):
    send_mail(
        'title',
        'contnet',
        "<contact@yebimom.com>",
        ["contact@yebimom.com"],
        fail_silently=False,
    )
