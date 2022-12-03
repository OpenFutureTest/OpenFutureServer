# -*- coding: utf8 -*-
import uuid
import time
import random
from datetime import datetime
import functools
from functools import wraps
from flask import json
from ofs import app
from ofs.common.xredis import Redis



def generate_id():
    return uuid.uuid1().hex


def unicode_byte_len(c):
    codepoint = ord(c)
    if codepoint <= 0x7f:
        return 1
    if codepoint <= 0x7ff:
        return 2
    if codepoint <= 0xffff:
        return 3
    if codepoint <= 0x10ffff:
        return 4
    return 5

'''The dictionary for the code of short url'''
CODE_DIC=('a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                                    '0','1','2','3','4','5','6','7','8','9')

def get_random_code(length=6):
    '''Get the code for short url'''
    code=""
    for i in range(length):
        code+=random.choice(CODE_DIC)
    return code

def unicode_string_len(s):
    return sum(map(unicode_byte_len, s))


def datetime2timestamp(dt):
    return time.mktime(dt.timetuple())


def str2timestamp(value):
    return time.mktime(time.strptime(value.strip(), "%Y-%m-%d %H:%M:%S"))


def timestamp2str(value):
    return datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')


def get_choices_desc(choices, value):
    for _value, _desc in choices:
        if value == _value:
            return _desc
    return None


class Lockit(object):
    def __init__(self, cache, key, expire=5, mock=False):
        self._cache = cache
        self._key = key
        self._expire = expire
        self._mock = mock

    def __enter__(self):
        if self._mock:
            return False
        if self._cache.get(self._key):
            return True
        self._cache.set(self._key, 1, self._expire)
        return False

    def __exit__(self, *args):
        if not self._mock:
            self._cache.delete(self._key)
        return False


def _cached_result(key_func, timeout=86400, snowslide=False, rtype='String'):
    """根据rtype参数选择相应的redis结构进行缓存
    rtype: String, Hash, Set, List, SortedSet
    """
    def wrapper(func):
        @wraps(func)
        def inner_func(*args):
            key = key_func(*args) if callable(key_func) else key_func
            result = None
            mock = not snowslide
            with Lockit(Redis, 'lock:%s' % (key), mock=mock) as locked:
                if locked:
                    time.sleep(0.5)
                else:
                    result = func(*args)
                    if rtype == 'Object' and result:
                        Redis.setex(key, timeout, json.dumps(result, 2))
                    elif rtype == 'Hash' and result:
                        Redis.hmset(key, result)
                        Redis.expire(key, timeout)
                    elif rtype == 'List':
                        Redis.delete(key)
                        # 处理结果为空数据, 防止穿透db, 在增加和查询的时候需要判断数据结构
                        Redis.rpush(key, *result) if result else Redis.set(key, 'empty')
                        Redis.expire(key, timeout)
                    elif rtype == 'Set':
                        Redis.delete(key)
                        # 处理结果为空数据, 防止穿透db, 在增加和查询的时候需要判断数据结构
                        Redis.sadd(key, *result) if result else Redis.set(key, 'empty')
                        Redis.expire(key, timeout)
                    elif rtype == 'SortedSet':
                        Redis.delete(key)
                        # 处理结果为空数据, 防止穿透db, 在增加和查询的时候需要判断数据结构
                        Redis.zadd(key, *result) if result else Redis.set(key, 'empty')
                        Redis.expire(key, timeout)
            return result
        return inner_func
    return wrapper

cached_object = functools.partial(_cached_result, rtype='Object')
cached_hash = functools.partial(_cached_result, rtype='Hash')
cached_set = functools.partial(_cached_result, rtype='Set')
cached_list = functools.partial(_cached_result, rtype='List')
cached_zset = functools.partial(_cached_result, rtype='SortedSet')


def get_url(uri, type=None):
    if uri is None or uri == "":
        return uri
    if uri.startswith("http"):
        return uri
    else:
        return app.config["STATIC_URL"] + uri