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

    def _name_parts(self, name):
        return (name[0:name.rindex('_')], name[name.rindex('_')+1:])

    def test_00_init(self):
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

    # test move group - extension
    def test_10_move_group(self):
        s, e = self._name_parts(conf.testgroup1['id'])
        resp = move_group(conf.testgroup1['id'], newext=e+'-next')
        assert resp == 200

    # test get group
    def test_11_get_group(self):
        resp = verify_group(conf.testgroup1, altid=conf.testgroup1['id']+'-next')
        assert resp == 200

    # test get history
    def test_12_get_history(self):
        expect = [
          {'activity': 'group', 'description': 'rename'}
        ]

        verify_history(conf.testgroup1, altid=conf.testgroup1['id']+'-next', expect_list=expect)

    # test delete group
    def test_13_delete_group(self):
        resp = delete_group(conf.testgroup1, altid=conf.testgroup1['id']+'-next')
        assert resp == 200
