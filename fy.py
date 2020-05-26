#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fy.py
# @Author: Jiang MJ
# @Date  : 2020/5/20
# @Desc  :
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Blueprint
from flask_login import login_required, current_user

fy = Blueprint('fy',__name__)


@fy.route('/fy')
@login_required
def hello():
    return render_template('index.html')


@fy.route('/fy/corder',methods=['GET','POST'])
@login_required
def corder():
    if request.method == 'GET':
        return render_template("corder.html")
    if request.method == 'POST':
        return 'baibai'