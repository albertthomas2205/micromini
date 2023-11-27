import pika, json, os, django
from django.http import JsonResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")
django.setup()


params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='user') # this will match the 
# routing key in the producer of the flask app


def callback(ch, method, properties, body):
    print('Received in Django microservice')
    print(body)
    data = json.loads(body)
    print(data)
    print('Added a comment')


channel.basic_consume(queue='user', on_message_callback=callback, \
auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
