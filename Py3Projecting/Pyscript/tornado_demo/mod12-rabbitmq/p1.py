import pika

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))                  #封装socket逻辑部分
channel = connection.channel()

channel.queue_declare(queue='hello')    #创建一个hello队列

channel.basic_publish(exchange='',
                      routing_key='hello',    #插入队列的名称
                      body='Hello World!')    #往队列里插入数据
print(" [x] Sent 'Hello World!'")
connection.close()