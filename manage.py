#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : manage.py
# @Author: Jiang MJ
# @Date  : 2020/5/18
# @Desc  :

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from app import app
from model import Users,Logs,Orders


db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()