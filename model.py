#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : model.py
# @Author: Jiang MJ
# @Date  : 2020/5/19
# @Desc  :

from flask_login import UserMixin
from flask_login._compat import unicode

from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class Users(db.Model,UserMixin):
    __tablername__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    tel = db.Column(db.String(11))
    #0 法院 1 不动产
    userid = db.Column(db.Boolean(), default=1, nullable=False)

    @property
    def password(self):
        raise ArithmeticError ('密码不可读')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return True
    def get_id(self):
        return unicode(self.id)


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #0新创建待审批 1已审批 2新提交待确认 3 已确认
    stats = db.Column(db.Integer, default=0, nullable=False)
    #0 查询 1查封
    orderid = db.Column(db.Integer, default=0, nullable=False)
    #查询或者查封主体标识（身份证号码）
    idcard = db.Column(db.String(18), nullable=False)
    filepath = db.Column(db.String(100))
    #备注
    remake = db.Column(db.String(200))
    create_time = db.Column(db.DateTime, default=datetime.datetime)

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer,db.ForeignKey('users.id'))
    orderid = db.Column(db.Integer,db.ForeignKey('orders.id'))
    opera = db.Column(db.String(100))
    #0失败 1成功
    op_stats = db.Column(db.Integer, default=1, nullable=False)


