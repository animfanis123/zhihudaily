#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from os import path

from peewee import SqliteDatabase
import redis


class Config(object):
    db = path.join(path.abspath(path.dirname(__file__)), 'zhihudaily.db')
    database = SqliteDatabase(db)
    redis_server = redis.StrictRedis(host='localhost', port=6379)


class DevelopConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False