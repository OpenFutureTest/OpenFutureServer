import os

BASE_DIR = os.path.abspath((os.path.dirname(__file__)))


class Local(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = '\x820\x91\xdb\x1cAQ\x1f\xa2\xa4\xb7)x\xdf\x8e\xb1%fZ\xfedm\xca\xdf'
    BASE_DIR = BASE_DIR
    STATIC_BASE = BASE_DIR + '/static'
    SERVER_URL = 'http://www.wodekouwei.com:8086'
    STATIC_URL = 'http://www.wodekouwei.com:8086'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    MYSQL_MASTER = {
        'name': 'ofs',
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'asd123456',
        'charset': 'utf8mb4'
    }

class Test(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = '\x820\x91\xdb\x1cAQ\x1f\xa2\xa4\xb7)x\xdf\x8e\xb1%fZ\xfedm\xca\xdf'
    BASE_DIR = BASE_DIR
    STATIC_BASE = "/data/storage"
    SERVER_URL = 'http://www.wodekouwei.com:8080'
    STATIC_URL = 'http://www.wodekouwei.com:8080'
    MEDIA_URL = 'http://www.wodekouwei.com:8080'
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    MYSQL_MASTER = {
        'name': 'ofs',
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'asd12345',
        'charset': 'utf8mb4'
    }