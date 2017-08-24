import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))                  #封装socket逻辑部分
channel = connection.channel()

channel.queue_declare(queue='hello')    #如果没有队列创建一个hello队列

def callback(ch, method, properties, body):     #定义操作需求的函数
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',    #取队列的名称
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()