#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from mydict import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        print("init")
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        print("init")
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        print("init")
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):

        print("init")
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        print("init")
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
     unittest.main()
     test_init()
     test_key()
     test_attr()
     test_keyerror()
     test_attrerror()
