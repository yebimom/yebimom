from celery import shared_task

from yebimom.settings import GOOGLE_API_KEY

import urllib
import requests
import json


@shared_task
def shorten_center_landing_url(center_landing_id, long_url):
    """
    Shorten CenterLanding url, and update instance
    """
    instance = CenterLanding.objects.get(id=center_landing_id)
    short_url = shorten_url(long_url)

    instance.shorten_url = short_url
    instance.save()


@shared_task
def shorten_url(long_url):
    """
    Generate shorten URL via goo.gl api
    - https://developers.google.com/url-shortener/v1/getting_started
    """

    BASE_URL = "https://www.googleapis.com/urlshortener/v1/url"
    params = {
        'key': GOOGLE_API_KEY,
    }
    headers = {'Content-Type': 'application/json'}
    data = {
        'longUrl': long_url
    }

    response = requests.post(BASE_URL, params=params, data=json.dumps(data), headers=headers)
    content = json.loads(response.content.decode('UTF-8'))
    short_url = content.get('id')

    return short_url


def url_builder(url, utm_source=None, utm_medium=None, utm_term=None, utm_content=None, utm_campaign=None):
    """
    URL Builder for Google Analytics
    - https://support.google.com/analytics/answer/1033867?hl=en
    """

    data = {}
    if utm_source:
        data['utm_source'] = utm_source
    if utm_medium:
        data['utm_medium'] = utm_medium
    if utm_term:
        data['utm_term'] = utm_term
    if utm_content:
        data['utm_content'] = utm_content
    if utm_campaign:
        data['utm_campaign'] = utm_campaign

    return url + "?" + urllib.urlencode(data)
