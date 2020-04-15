import time
import os

from nose.tools import *

import settings as conf
from test.testlib import *

import logging.config
logger = logging.getLogger(__name__)

#
# group members tests
#


class Member_Test():

    def test_00_init(self):
        stat = delete_group(conf.testgroup2)
        assert stat == 200 or stat == 404
        stat = build_group(conf.testgroup2)
        assert stat == 201

    # test add members
    def test_01_add_members(self):
        stat, resp = add_members(conf.testgroup2, conf.members1)
        assert stat == 200

    # test verify add members
    def test_02_verify_members(self):
        # this one to cache
        stat = verify_members(conf.testgroup2, conf.members1)
        assert stat == 200
        # this one to registry
        stat = verify_members(conf.testgroup2, conf.members1, True)
        assert stat == 200

    # test set membership
    def test_03_set_membership(self):
        stat, resp = set_membership(conf.testgroup2, conf.members2)
        assert stat == 200
        assert len(resp['errors'][0]['notFound']) == 0

    # test verify set members
    def test_04_verify_set_members(self):
        # this one to registry
        stat = verify_members(conf.testgroup2, conf.members2, True)
        assert stat == 200
        # this one to cache
        stat = verify_members(conf.testgroup2, conf.members2)
        assert stat == 200

    # test set membership with bogus member
    def test_05_set_membership(self):
        stat, resp = set_membership(conf.testgroup2, conf.members2not)
        assert stat == 200
        assert resp['errors'][0]['status'] == 200
        assert resp['errors'][0]['notFound'][0] == '0joeuser'

    # test cleanup
    def test_99_cleanup(self):
        stat = delete_group(conf.testgroup2)
        assert stat == 200
