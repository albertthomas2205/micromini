import pika, json

params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print(method,body)
    print("hellloooooooooooo")
    properties = pika.BasicProperties(content_encoding='application/json',delivery_mode=2)
    channel.basic_publish(exchange='', routing_key='user', \
    body=json.dumps(body), properties=properties) 
    # routing key here must match the queue name in the consumer\
    # of the flask app
