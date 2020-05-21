#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: Jiang MJ
# @Date  : 2020/5/18
# @Desc  :
import os
DEBUG = True

SECRET_KEY =os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'fybdc'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DIALECT,
        DRIVER,
        USERNAME,
        PASSWORD,
        HOST,
        PORT,
        DATABASE
    )

SQLALCHEMY_TRACK_MODIFICATIONS = True

# class Config:
#
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to gusess string'
#
#     DIALECT = 'mysql'
#     DRIVER = 'pymysql'
#     USERNAME = 'root'
#     PASSWORD = 'root'
#     HOST = '127.0.0.1'
#     PORT = '3306'
#     DATABASE = 'fybdc'
#
#     SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
#         DIALECT,
#         DRIVER,
#         USERNAME,
#         PASSWORD,
#         HOST,
#         PORT,
#         DATABASE
#     )
#
#     # 便于调试
#     TEMPLATES_AUTO_RELOAD = True
#     SEND_FILE_MAX_AGE_DEFAULT = 0
