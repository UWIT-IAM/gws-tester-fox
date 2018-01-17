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
        resp = delete_group(conf.testgroup2)
        assert resp == 200 or resp == 404
        resp = build_group(conf.testgroup2)
        assert resp == 201

    # test add members
    def test_01_add_members(self):
        resp = add_members(conf.testgroup2, conf.members1)
        assert resp == 200

    # test verify add members
    def test_02_verify_members(self):
        resp = verify_members(conf.testgroup2, conf.members1)
        assert resp == 200
        resp = verify_members(conf.testgroup2, conf.members1, True)
        assert resp == 200

    # test set membership
    def test_03_set_membership(self):
        resp = set_membership(conf.testgroup2, conf.members2)
        assert resp == 200

    # test verify set members
    def test_04_verify_set_members(self):
        resp = verify_members(conf.testgroup2, conf.members2)
        assert resp == 200
        resp = verify_members(conf.testgroup2, conf.members2, True)
        assert resp == 200

    # test cleanup
    def test_99_cleanup(self):
        resp = delete_group(conf.testgroup2)
        assert resp == 200
