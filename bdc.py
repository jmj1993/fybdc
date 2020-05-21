#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bdc.py
# @Author: Jiang MJ
# @Date  : 2020/5/20
# @Desc  :

from flask import Blueprint
from flask_login import login_required


bdc = Blueprint('bdc',__name__)


@bdc.route('/bdc')
@login_required
def hello():
    return 'bdc'