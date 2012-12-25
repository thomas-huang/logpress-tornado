#!/usr/bin/env python
#encoding=utf-8
import os

DEBUG = True

BLOG_NAME = u'Logpress'
SITE_DESC= """blog powered by tornado,jinja2,peewee"""
DOMAIN='http://0.0.0.0:9000'

THEME_NAME = 'fluid-blue'

DB_ENGINE = 'peewee.SqliteDatabase'  # peewee.SqliteDatabase,peewee.MySQLDatabase
DB_HOST= '0.0.0.0'
DB_USER = 'root'
DB_PASSWD = 'root'
DB_NAME = os.path.join(os.path.dirname(__file__),'blog.db')  #db file if DB_ENGINE is SqliteDatabase