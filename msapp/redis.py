import redis
from django.conf import settings


class RedisFactory(object):
    _pool = redis.ConnectionPool(host=settings.REDIS['HOST'],
                                 port=settings.REDIS['PORT'],
                                 socket_timeout=settings.REDIS['TIMEOUT'],
                                 db=settings.REDIS['DB'])

    @classmethod
    def create(cls):
        return redis.StrictRedis(connection_pool=cls._pool)
