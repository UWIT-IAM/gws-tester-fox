import time
import os

from nose.tools import *

import settings as conf
from test.testlib import *

import logging.config
logger = logging.getLogger(__name__)

#
# basics tests:  odd errors and etc
#


def _basics_verify_base(ext, vstatus, vres=None):
    status, data = get_resource(ext)
    assert status == vstatus
    assert data['schemas'][0] == conf.SCHEMA
    meta = data['meta']
    if vres is not None:
        assert meta['resourceType'] == vres
    assert meta['timestamp'] > 0
    return data


def _basics_verify_error(ext, stat, res=None):
    data = _basics_verify_base(ext, stat, res)
    assert data['errors'][0]['status'] == stat
    assert len(data['errors'][0]['detail'][0]) > 0
    print('stat=%d, detail=%s' % (stat, data['errors'][0]['detail'][0]))


class Basics_Test():

    def test_00_base(self):
        _basics_verify_base('/group/u_fox_00-spud99', 200)

    def test_01_group(self):
        _basics_verify_error('/group', 400, 'group')

    def test_02_nogroup(self):
        _basics_verify_error('/group/not_a_group', 404, 'group')

    def test_03_search(self):
        _basics_verify_error('/search', 400, 'search')

    def test_04_badreq(self):
        _basics_verify_error('/spud', 400)

    def test_05_badreq(self):
        _basics_verify_error('/group/not_a_group/member', 404)

    def test_06_badreq(self):
        _basics_verify_error('/group/not_a_group/member/not_a_member', 404)

    def test_10_badreq(self):
        _basics_verify_error('/group$<xml>/', 400)

    def test_11_badreq(self):
        _basics_verify_error('/group/{xx=1}', 404)
