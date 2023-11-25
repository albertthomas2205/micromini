import pika, json, os, django
from django.http import JsonResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin') # this will match the 
# routing key in the producer of the flask app


def callback(ch, method, properties, body):
    print('Received in Django microservice')
    print(body)
    data = json.loads(body)
    print('Added a comment')


channel.basic_consume(queue='admin', on_message_callback=callback, \
auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

# import pika

# params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# channel.queue_declare(queue='admin')


# def callback(ch,method,properties,body):
#     print("received in admin")
#     print(body)
# channel.basic_consume(queue='admin',on_message_callback=callback)

# print("started consuming")

# channel.start_consuming()

# channel.close()

# import pika

# def callback(body):
#     print("Received message:")
#     print(body.decode())

# def start_consuming():
#     # RabbitMQ connection parameters
#     params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

#     # Establish a connection
#     connection = pika.BlockingConnection(params)
#     channel = connection.channel()

#     # Declare the queue
#     channel.queue_declare(queue='admin')

#     # Set up the consumer
#     channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

#     print("Started consuming. Press Ctrl+C to exit.")

#     # Start consuming messages
#     channel.start_consuming()


#     # Start consuming messages
# start_consuming()

# import pika

# # RabbitMQ connection parameters
# params = pika.URLParameters("amqp://guest:guest@localhost:5672/")

# # Establish a connection
# connection = pika.BlockingConnection(params)
# channel = connection.channel()

# # Declare the queue
# channel.queue_declare(queue='admin')

# def callback(ch, method, properties, body):
#     print(f"Received message from producer: {body.decode()}")

# # Set up the consumer
# channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

# print("Started consuming. Press Ctrl+C to exit.")

# # Start consuming messages
# channel.start_consuming()




