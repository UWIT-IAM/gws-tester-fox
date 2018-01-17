import time
import os

from nose.tools import *

import settings as conf
from test.testlib import *

import logging.config
logger = logging.getLogger(__name__)

#
# group affiliate tests
#
# includes minimal history
#


class Affiliate_Test():

    def test_00_init(self):
        resp = delete_group(conf.testgroup2)
        assert resp == 200 or resp == 404
        resp = build_group(conf.testgroup2)
        assert resp == 201

    # test set google
    def test_010_set_google(self):
        resp = put_affiliate(conf.testgroup2, conf.google_affiliate_1)
        assert resp == 200

    # test verify google
    def test_020_verify_google(self):
        resp = verify_affiliate(conf.testgroup2, conf.google_affiliate_1)
        assert resp == 200

    # test verify google
    def test_021_verify_google(self):
        resp = verify_group(conf.testgroup2, conf.google_affiliate_1)
        assert resp == 200

    # test set google
    def test_030_verify_google(self):
        resp = put_affiliate(conf.testgroup2, conf.google_affiliate_2)
        assert resp == 200

    # test verify google
    def test_040_verify_google(self):
        resp = verify_affiliate(conf.testgroup2, conf.google_affiliate_2)
        assert resp == 200

    # test verify google
    def test_041_verify_google(self):
        resp = verify_group(conf.testgroup2, conf.google_affiliate_2)
        assert resp == 200

    # test set bogus gooogle sender fails 403
    def test_047_set_bogus_google(self):
        resp = put_affiliate(conf.testgroup2, conf.google_affiliate_3)
        assert resp == 403

    # test set email on google fails 403
    def test_048_set_bogus_email(self):
        resp = put_affiliate(conf.testgroup2, conf.email_affiliate_1)
        assert resp == 403

    # test clear google
    def test_09_clear_google(self):
        resp = put_affiliate(conf.testgroup2, conf.google_affiliate_9)
        assert resp == 200

    # test set email
    def test_11_set_email(self):
        resp = put_affiliate(conf.testgroup2, conf.email_affiliate_1)
        assert resp == 200

    # test verify email
    def test_120_verify_email(self):
        resp = verify_affiliate(conf.testgroup2, conf.email_affiliate_1)
        assert resp == 200

    # test verify email
    def test_121_verify_email(self):
        resp = verify_group(conf.testgroup2, conf.email_affiliate_1)
        assert resp == 200

    # test set email
    def test_13_set_email(self):
        resp = put_affiliate(conf.testgroup2, conf.email_affiliate_2)
        assert resp == 200

    # test verify email
    def test_140_verify_email(self):
        resp = verify_affiliate(conf.testgroup2, conf.email_affiliate_2)
        assert resp == 200

    # test verify email
    def test_141_verify_email(self):
        resp = verify_group(conf.testgroup2, conf.email_affiliate_2)
        assert resp == 200

    # test clear email
    def test_19_clear_email(self):
        resp = put_affiliate(conf.testgroup2, conf.email_affiliate_9)
        assert resp == 200

    def test_81_history(self):
        resp = verify_history(conf.testgroup2, 15)
        assert resp == 200

    # test cleanup
    def test_99_cleanup(self):
        print('cleanup')
        resp = delete_group(conf.testgroup2)
        assert resp == 200
