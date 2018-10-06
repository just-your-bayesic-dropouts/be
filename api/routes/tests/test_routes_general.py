#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.test_base import BaseTestCase


class TestBasic(BaseTestCase):

    def setUp(self):
        super(TestBasic, self).setUp()
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_default(self):
        return True
