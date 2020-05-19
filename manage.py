#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : manage.py
# @Author: Jiang MJ
# @Date  : 2020/5/18
# @Desc  :

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model import *
# from exts import db
from app import app


manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.config.from_pyfile("config.py")
    db.init_app(app)

    manage.run()