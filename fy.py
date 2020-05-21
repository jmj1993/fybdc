#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fy.py
# @Author: Jiang MJ
# @Date  : 2020/5/20
# @Desc  :
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Blueprint
from flask_login import login_required

fy = Blueprint('fy',__name__)


@fy.route('/fy')
@login_required
def hello():
    return render_template('index.html')