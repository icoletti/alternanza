
"""
Configuration file
"""

import os
import redis
REDIS_URL = os.environ["REDIS_URL"]
DEBUG_MODE = os.environ.get('DEBUG', 'False').lower() in ['true', '1']


class Config(object):
    """ config object """
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = os.environ['SECRET_KEY']

    # redis config
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url(REDIS_URL)

    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 100
    CACHE_REDIS_URL = REDIS_URL

    DEBUG = DEBUG_MODE