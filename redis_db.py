# coding: utf-8

import redis

pool = redis.ConnectionPool(host='118.24.155.213', port=6379, password='yehui', db=0)
r = redis.StrictRedis(connection_pool=pool)


def event_handler(data):
    data = str(data['data'], encoding='utf-8')
    print(data)


# 创建发布订阅对象
psub = r.pubsub()
# 发布监听key失效的订阅
psub.psubscribe(**{'__keyevent@0__:expired': event_handler})
thread = psub.run_in_thread(sleep_time=0.01)