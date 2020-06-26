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

    # find via in search
    def _find_via(self, data, id, via):
        for g in data:
            if g['id'] == id:
                if 'via' in g:
                    for sub in g['via']:
                        if sub == via:
                            return True
        return False

    # create first group
    def test_01_create_group(self):
        stat = delete_group(conf.testgroup1)
        assert stat == 200 or stat == 404
        stat = build_group(conf.testgroup1)
        assert stat == 200 or stat == 201 or stat == 412

    # create second group
    def test_02_create_group(self):
        stat = delete_group(conf.testgroup2)
        assert stat == 200 or stat == 404
        stat = build_group(conf.testgroup2)
        assert stat == 200 or stat == 201 or stat == 412

    # create third group
    def test_03_create_group(self):
        stat = delete_group(conf.testgroup3)
        assert stat == 200 or stat == 404
        stat = build_group(conf.testgroup3)
        assert stat == 200 or stat == 201 or stat == 412

    # add member=group2 to group1
    def test_04_add_members(self):
        stat, resp = add_members(conf.testgroup1, [
                {"type": "group", "id": conf.testgroup2['id']}
            ])
        assert stat == 200

    # add member=group3, joeuser to group2
    def test_05_add_members(self):
        stat, resp = add_members(conf.testgroup2, [
                {"type": "group", "id": conf.testgroup3['id']},
                {"type": "uwnetid", "id": "joeuser"}
            ])
        assert stat == 200

    # add member=lisas22g to group3
    def test_06_add_members(self):
        stat, resp = add_members(conf.testgroup3, [
                {"type": "uwnetid", "id": "lisas22g"}
            ])
        assert stat == 200

    # test stem search
    def test_11_search(self):
        (stat, data) = search_groups(stem=conf.GROUP_BASE, scope="one")
        assert stat == 200
        # print (data)
        assert self._find_id(data, conf.GROUP_BASE)
        assert self._find_id(data, conf.testgroup1['id'])
        assert self._find_id(data, conf.testgroup2['id'])
        assert not self._find_id(data, conf.testgroup3['id'])

    def test_11a_search(self):
        (stat, data) = search_groups(stem=conf.GROUP_BASE, scope="all")
        assert stat == 200
        # print (data)
        assert self._find_id(data, conf.GROUP_BASE)
        assert self._find_id(data, conf.testgroup1['id'])
        assert self._find_id(data, conf.testgroup2['id'])
        assert self._find_id(data, conf.testgroup3['id'])

    # test name search
    def test_12_search(self):
        (stat, data) = search_groups(name='*' + conf.testgroup2['id'][6:] + '*')
        assert stat == 200
        print(data)
        assert self._find_id(data, conf.testgroup2['id'])
        assert self._find_id(data, conf.testgroup3['id'])

    # test member search
    def test_13_search(self):
        (stat, data) = search_groups(member="lisas22g", type="direct")
        assert stat == 200
        assert self._find_id(data, conf.testgroup3['id'])

    def test_14_search(self):
        (stat, data) = search_groups(member="lisas22g", type="effective")
        assert stat == 200
        assert self._find_id(data, conf.testgroup1['id'])
        assert self._find_id(data, conf.testgroup2['id'])
        assert self._find_id(data, conf.testgroup3['id'])
        assert self._find_via(data, conf.testgroup1['id'], conf.testgroup2['id'])
        assert self._find_via(data, conf.testgroup1['id'], conf.testgroup3['id'])

    # cleanup
    def test__99_cleanup(self):
        stat = delete_group(conf.testgroup3)
        assert stat == 200
        stat = delete_group(conf.testgroup2)
        assert stat == 200
        stat = delete_group(conf.testgroup1)
        assert stat == 200
