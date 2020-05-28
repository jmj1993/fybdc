#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : utils.py
# @Author: Jiang MJ
# @Date  : 2020/5/28
# @Desc  :
import os

from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))

def upload(f):
    upload_path = os.path.join(basedir, 'static/upload/')
    file_name = upload_path + secure_filename(f.filename)
    f.save(file_name)
    return secure_filename(f.filename)