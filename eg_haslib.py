#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print("md5 "+md5.hexdigest())

md52 = hashlib.md5() #show multi str has the same result
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))
print("md52 "+md52.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print("sha1 "+sha1.hexdigest())
