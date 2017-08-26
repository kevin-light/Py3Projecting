import redis

#先运行启动服务端  redis-server

rt = redis.Redis(host='127.0.0.1',port=6379)
rt.set('foo','bar')
print(rt.get('foo'))