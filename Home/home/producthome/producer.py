import pika

params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='home',body = 'hello')