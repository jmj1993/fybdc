#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fy.py
# @Author: Jiang MJ
# @Date  : 2020/5/20
# @Desc  :
import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Blueprint
from flask_login import login_required, current_user

from exts import db
from utils import upload
from model import Orders


fy = Blueprint('fy',__name__)


@fy.route('/fy')
@login_required
def hello():
    ord = Orders.query.all()
    allord = len(ord)






    return render_template('index.html',allord =len(ord),ords =ord)


@fy.route('/fy/corder',methods=['GET','POST'])
@login_required
def corder():
    if request.method == 'GET':
        return render_template("corder.html")
    if request.method == 'POST':
        f = request.files["file"]
        url = upload(f,'fy/')
        idc = request.form["title"]
        oid = request.form["city"]
        rema = request.form["desc"]
        ord = Orders(orderid = oid,idcard = idc,filepath = '/fy/'+url,remake =rema)
        db.session.add(ord)
        db.session.commit()
        res = {
            "code": 0

        }
        flash('添加成功')
        return redirect(url_for('home'))