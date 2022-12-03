# -*- coding: utf8 -*-
from flask import Flask, request
from flask.json import JSONEncoder

import logging
import os

__all__ = ["app"]

# 通过环境变量来进行配置切换
env = os.environ.get('OFSENV')
if env not in ['Local', 'Test', 'Stage', 'Production', 'UnitTest']:
    raise EnvironmentError('The environment variable (OFSENV) is invalid')



app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config.from_object("config.%s" % (env))

# async = os.environ.get('OFSASYNC')


@app.before_request
def before_request():
    '''
    from osn.base.xmysql import MYDB
    MYDB.connect()
    '''
    request.authed_user = None

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


# 日志记录
from ofs.common.log import appHandler

app.logger.setLevel(logging.WARNING)
app.logger.addHandler(appHandler)
import ofs.views.user
'''
if async == 'YES':
    pass
else:
    
'''