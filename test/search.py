import time
import os

from nose.tools import *

import settings as conf
from test.testlib import *

import logging.config
logger = logging.getLogger(__name__)

#
# search tests
#


class Search_Test():

    # find id in search
    def _find_id(self, data, id):
        for g in data:
            if g['id'] == id:
                return True
        return False

    # test create first group
    def test_01_create_group(self):
        resp = build_group(conf.testgroup1)
        assert resp == 200 or resp == 201 or resp == 412

    # test create second group
    def test_02_create_group(self):
        resp = build_group(conf.testgroup2)
        assert resp == 200 or resp == 201 or resp == 412

    # test search
    def test_03_search(self):
        (resp, data) = search_groups(stem=conf.GROUP_BASE, scope="one")
        assert resp == 200
        # print (data)
        assert self._find_id(data, conf.GROUP_BASE)
        assert self._find_id(data, conf.testgroup1['id'])
        assert self._find_id(data, conf.testgroup2['id'])

    # cleanup
    def test__99_cleanup(self):
        resp = delete_group(conf.testgroup1)
        assert resp == 200
        resp = delete_group(conf.testgroup2)
        assert resp == 200