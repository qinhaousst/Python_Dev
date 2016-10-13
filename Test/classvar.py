#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'qinhao'


import hashlib

hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()