# -*- coding: utf8 -*-
import time
import traceback
from functools import wraps

from flask import jsonify, request

from ofs.models.user import User
from ofs.common import error, httperror
from ofs.common.log import print_log


def jsonapi(login_required=False):
    """API接口统一处理
    """
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            start = int(time.time() * 1000)
            try:
                ut = request.values.get("ut", None)
                user = None
                if ut is None:
                    body = request.get_json()
                    if body is not None:
                        ut = body.get("ut", None)
                if ut is not None:
                    uid = User.uid_from_token(ut)
                    user = User.get_one(uid)
                    request.authed_user = user
                if login_required and not user:
                    data = error.AuthRequired
                else:
                    data = func(*args, **kwargs)
                status = data.errno if isinstance(data, error.ApiError) else 0
                errmsg = data.errmsg if isinstance(data, error.ApiError) else '成功'
                errname = data.name if isinstance(data, error.ApiError) else ''
                if data is None or isinstance(data, error.ApiError):
                    data = {}
            except:
                print_log('app', '%s%s' % (traceback.format_exc(), request.values))
                status, errmsg, errname, data = -1, u'服务器异常', 'Internal Server Error', {}
            result = {
                'status': status,
                'errmsg': errmsg,
                'error': errname,
                'data': data,
                'time': int(time.time() * 1000) - start,
            }
            return jsonify(result)
        return decorated_function
    return decorator


def json_input(required_args=None):
    def json_body(func):
        @wraps(func)
        def check(*args, **kws):
            if "application/json" not in request.headers.get('Content-Type', ''):
                raise httperror.InvalArguments("Content-Type must be application/json.")
            body = request.get_json()
            if body is None:
                raise httperror.InvalArguments("Invalid POST body!")
            if required_args is not None:
                for item in required_args:
                    if item not in body:
                        raise httperror.MissArguments("%s is required!", item)
            return func(*args, **kws)
        return check
    return json_body

