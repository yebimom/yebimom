#!/usr/bin/env python
# encoding: utf-8

"""
Make centers fixture from crawling xml data by Naver Search API
"""

from centers.utils.center_hashids import get_encoded_center_hashid
from bs4 import BeautifulSoup
import re
import requests
import os
from time import sleep


def populate_tags_value(tags, tmp_center_fixture):
    tmp_center_fixture = tmp_center_fixture.replace(
        'TITLE', tags['title']
    )
    tmp_center_fixture = tmp_center_fixture.replace(
        'ADDRESS', tags['address']
    )
    tmp_center_fixture = tmp_center_fixture.replace(
        'TELEPHONE', tags['telephone']
    )
    tmp_center_fixture = tmp_center_fixture.replace(
        'LINK', tags['link']
    )
    tmp_center_fixture = tmp_center_fixture.replace(
        'LONGITUDE', tags['longitude']
    )
    tmp_center_fixture = tmp_center_fixture.replace(
        'LATITUDE', tags['latitude']
    )
    tmp_center_fixture = tmp_center_fixture.replace(
        'HASH', tags['hashid']
    )

    return tmp_center_fixture


def fixture_value_formatter(*args):
    tags = ()
    for arg in args:
        try:
            tags += (('"' + re.sub('[\r\t\n]', '', arg[0].text) + '"'),)
        except IndexError:
            """
            If Tag instance but not have index
            """
            tags += ('""',)
        except AttributeError:
            '''
            If string, not Tag instance
            '''
            if arg is "null":
                tags += (arg,)
            else:
                tags += (('"' + re.sub('[\r\t\n]', '', arg) + '"'),)

    return tags


def get_daum_api_trans_coord_kmt_to_wgs_url(mapx, mapy):
    try:
        DAUM_API_KEY = os.environ['DAUM_API_KEY']
    except KeyError:
        DAUM_API_KEY = ''

    domain = "http://apis.daum.net/"
    request_purpose_url = "maps/transcoord"
    daum_api_key = "?apikey=%s" % (DAUM_API_KEY)

    # coordinate parameters only contain numeric values
    mapx = re.sub('"', '', mapx)
    mapy = re.sub('"', '', mapy)

    tm128_coordinates = "&x=%s&y=%s" % (mapx, mapy)
    trans_coord_name_url = "&fromCoord=KTM&toCoord=WGS84"
    request_output_format = "&output=xml"
    target_url = domain + request_purpose_url + daum_api_key + \
        tm128_coordinates + trans_coord_name_url + request_output_format

    return target_url


def get_wgs_coord_category_using_requests(target_url):
    sleep(0.1)
    response = requests.get(target_url)

    try:
        bs_wgs_coord_xml = BeautifulSoup(response.text, 'xml')
    except:
        return False
    print bs_wgs_coord_xml
    try:
        wgs_coord_category = bs_wgs_coord_xml('result')[0]
    except:
        return False

    return wgs_coord_category


def ktm_to_wgs(mapx, mapy):
    target_url = get_daum_api_trans_coord_kmt_to_wgs_url(mapx, mapy)
    wgs_coord_category = get_wgs_coord_category_using_requests(target_url)

    if wgs_coord_category is False:
        longitude, latitude = "null", "null"
    else:
        longitude, latitude = (
            wgs_coord_category.attrs.get('x'),
            wgs_coord_category.attrs.get('y')
        )

    return (longitude, latitude)


def populate_center_fixture(item, tmp_center_fixture, id):
    title, address, telephone, link, mapx, mapy, hashid = \
        fixture_value_formatter(
            item('title'),
            item('address'),
            item('telephone'),
            "null",
            item('mapx'),
            item('mapy'),
            get_encoded_center_hashid(id)
        )

    longitude, latitude = ktm_to_wgs(mapx, mapy)

    tags = {
        'title': title,
        'address': address,
        'telephone': telephone,
        'link': link,
        'longitude': longitude,
        'latitude': latitude,
        'hashid': hashid
    }

    tmp_center_fixture = populate_tags_value(tags, tmp_center_fixture)

    return tmp_center_fixture


def populate_all_centers_fixture(
    sample_center_fixture,
    bs_centers_info,
    centers_fixture_f
):
    centers_fixture_f.write('[\n')

    fixture_cycle = 1
    tmp_center_fixture = sample_center_fixture
    all_centers_fixture = ''

    for item in bs_centers_info:
        tmp_center_fixture = populate_center_fixture(
            item,
            tmp_center_fixture,
            fixture_cycle
        )

        all_centers_fixture += tmp_center_fixture

        fixture_cycle += 1
        tmp_center_fixture = sample_center_fixture

    """
    Last json field must not have ','
    """

    all_centers_fixture = re.sub(',$', '', all_centers_fixture).encode('utf-8')
    centers_fixture_f.write(all_centers_fixture)
    centers_fixture_f.write(']')


def make_centers_item_info(centers_full_info_f):
    # Beautiful soup instance
    bs_centers_item_info = \
        BeautifulSoup(centers_full_info_f.read(), 'xml')('item')
    return bs_centers_item_info


def open_center_info_files():
    sample_center_fixture_f = open('sample-center-fixture.json', 'r')
    centers_full_info_f = open('centers-data.xml', 'r')
    centers_fixture_f = open('centers-fixture.json', 'w+')

    return (sample_center_fixture_f, centers_full_info_f, centers_fixture_f)


def close_files(*args):
    for arg in args:
        arg.close()


def make_centers_fixture():
    sample_center_fixture_f, centers_full_info_f, centers_fixture_f = \
        open_center_info_files()

    sample_center_fixture = sample_center_fixture_f.read()
    bs_centers_info = make_centers_item_info(centers_full_info_f)

    populate_all_centers_fixture(
        sample_center_fixture,
        bs_centers_info,
        centers_fixture_f
    )

    close_files(
        sample_center_fixture_f,
        centers_full_info_f,
        centers_fixture_f
    )

make_centers_fixture()
