# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir

app = Flask(__name__)

app.config.from_object('config')#载入配置文件

db = SQLAlchemy(app)# 初始化数据库管理对象

from . import views,models