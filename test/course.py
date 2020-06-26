import time
import os

from nose.tools import *

import settings as conf
from test.testlib import *

import logging.config
logger = logging.getLogger(__name__)


#
# course tests
#
class Course_Test():

    # find and get some course groups
    # search form them by sln
    # compare results
    # if phys drops the 121 course this won't work

    def test_01_course(self):
        # get some courses.  we'll want the slns
        (year, qtr, groups) = find_some_courses('phys', '121')
        base_groups = {}
        base_ids = set()
        slns = []
        for group in groups:
            (st, grp) = get_resource('/group/' + group['id'])
            base_groups[grp['data']['id']] = grp['data']
            base_ids.add((grp['data']['id']))
            slns.append(grp['data']['course']['sln'])

        # get the same groups via an sln searh
        (st, groups) = get_resource('/search?year=%d&quarter=%s&sln=%s' % (year, qtr, ','.join(slns)))

        # verify we found the same groups
        for group in groups['data']:
            assert(group['id'] in base_ids)
            base = base_groups[group['id']]
            assert(group['curriculum'] == base['course']['curriculum'])
            assert(group['number'] == base['course']['number'])
            assert(group['section'] == base['course']['section'])
