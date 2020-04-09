# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, session, url_for, request, g,Response, json, jsonify
from app import app, db
from .models import User, Post
# , ROLE_USER, ROLE_ADMIN

@app.route('/')
def index():
    return  'hello world,hello flasker'

@app.route('/adduser/nickname=<string:nickname>&email=<string:email>')
def adduser(nickname, email):
    u = User(nickname=nickname, email=email)
    try:
        db.session.add(u)
        db.session.commit()
        return '添加成功'
    except Exception as e:
        return '用户名或邮箱已存在'

@app.route('/getuser/<nickname>')
def getuser(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    try:
        jsonarr = {
            'username': user.nickname,
            'email': user.email
        }
        return Response(json.dumps(jsonarr), content_type='application/json')
    except Exception as e:
        return '用户名输入错误'

@app.route('/all')
def all():
    user = User.query.all()
    payload = []
    for result in user:
        content = {'id': result.id, 'username': result.nickname, 'email': result.email, 'role': result.role}
        payload.append(content)
        content = {}
    return jsonify(payload)