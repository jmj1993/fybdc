#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : model.py
# @Author: Jiang MJ
# @Date  : 2020/5/19
# @Desc  :

from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class Users(db.Model):
    __tablername__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tel = db.Column(db.String(11))
    #0 法院 1 不动产
    userid = db.Column(db.Boolean(), default=1, nullable=False)

    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #0新创建待审批 1已审批 2新提交待确认 3 已确认
    stats = db.Column(db.Integer, default=0, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime)

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer,db.ForeignKey('users.id'))
    orderid = db.Column(db.Integer,db.ForeignKey('orders.id'))
    opera = db.Column(db.String(100))
    #0失败 1成功
    op_stats = db.Column(db.Integer, default=1, nullable=False)


