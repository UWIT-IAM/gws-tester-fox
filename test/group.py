import time
import os

from nose.tools import *

import settings as conf
from test.testlib import *

import logging.config
logger = logging.getLogger(__name__)

#
# group tests
#


class Group_Test():

    def __init__(self):
        resp = delete_group(conf.testgroup1)
        assert resp == 200 or resp == 404

    # test create group
    def test_01_create_group(self):
        resp = build_group(conf.testgroup1)
        assert resp == 201

    # test get group
    def test_02_get_group(self):
        resp = verify_group(conf.testgroup1)
        assert resp == 200

    # test delete group
    def test__03_delete_group(self):
        resp = delete_group(conf.testgroup1)
        assert resp == 200
