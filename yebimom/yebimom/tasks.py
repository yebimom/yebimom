# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import shared_task

# Email
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

# Configuration variables
from yebimom.settings.partials.application import \
    API_STORE_SMS_KEY, API_STORE_SMS_BASE_URL, SMS_SEND_PHONE

import requests


def _send_question_email_to_admin(email, phone, title, content):
    email_template = get_template('email/admin/contact/question.html')
    email_context = Context({
        'email': email,
        'phone': phone,
        'title': title,
        'content': content,
    })

    # send email to admin
    send_mail(
        "[1:1 문의] " + title.encode('utf-8'),
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        ["contact@yebimom.com"],
        fail_silently=False,
    )


def _send_question_email_to_user(email, content):
    email_template = get_template('email/contact/question.html')
    email_context = Context({
        'content': content
    })

    # send email to user
    send_mail(
        "[예비맘파트너스] 1:1 문의가 등록되었습니다",
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        [email],
        fail_silently=False,
    )


def _send_answer_email_to_admin(email, phone, question_title, content):
    email_template = get_template('email/admin/contact/answer.html')
    email_context = Context({
        'email': email,
        'phone': phone,
        'question_title': question_title,
        'content': content,
    })

    # send email to admin
    send_mail(
        "[1:1 문의 답변] " + question_title.encode('utf-8'),
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        ["contact@yebimom.com"],
        fail_silently=False,
    )


def _send_answer_email_to_user(email, question_title, content):
    email_template = get_template('email/contact/answer.html')
    email_context = Context({
        'content': content
    })

    # send email to user
    send_mail(
        "[1:1 문의 답변] : " + question_title.encode('utf-8'),
        email_template.render(email_context),
        "예비맘 <contact@yebimom.com>",
        [email],
        fail_silently=False,
    )


def _send_sms(phone, username, data):
    headers = {
        'x-waple-authorization': API_STORE_SMS_KEY
    }

    sms_data = {
        'dest_phone': phone,
        'dest_name': username,
        'send_phone': SMS_SEND_PHONE,
        'send_name': "예비맘파트너스",
    }
    sms_data.update(data)

    requests.post(
        API_STORE_SMS_BASE_URL, data=sms_data, headers=headers
    )


@shared_task
def send_center_landing_sms(phone, name, center, url):
    phone = phone.encode('utf-8')
    name = name.encode('utf-8')
    center = center.encode('utf-8')
    url = url.encode('utf-8')

    # Send SMS to User
    data = {
        'msg_body': "[%s] %s님, 산후조리원 이벤트에 신청되었습니다. %s" % (center, name, url),
    }
    _send_sms(phone, name, data)

    # Send SMS to CenterAdmin
    data = {
        'msg_body': "[모두의 산후조리원] 새로운 이벤트 신청 ( %s / %s )" % (name, phone),
    }
    _send_sms("01022205736", "모두의 산후조리원", data)


@shared_task
def send_question_email(email, phone, title, content):
    _send_question_email_to_user(email, content)
    _send_question_email_to_admin(email, phone, title, content)


@shared_task
def send_answer_email(email, phone, question_title, content):
    _send_answer_email_to_user(email, question_title, content)
    _send_answer_email_to_admin(email, phone, question_title, content)


@shared_task
def send_question_sms(phone, username):
    data = {
        'msg_body': "[예비맘파트너스] 1:1 문의가 등록되었습니다",
        'subject': "[예비맘파트너스] 1:1 문의 등록 완료"
    }
    _send_sms(phone, username, data)


@shared_task
def send_answer_sms(phone, username):
    data = {
        'msg_body': "[예비맘파트너스] 1:1 문의 답변이 등록되었습니다",
        'subject': "[예비맘파트너스] 1:1 문의 답변 완료"
    }
    _send_sms(phone, username, data)
