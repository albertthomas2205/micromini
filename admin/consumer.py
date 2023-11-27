import pika, json, os, django
from django.http import JsonResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.producer import publish
from products.views import ProductViewSet

params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin') # this will match the 
# routing key in the producer of the flask app


# def callback(ch, method, properties, body):
#     print('Received in Django admin microservice')
#     print(body)
    
#     # Create an instance of ProductViewSet
#     obj = ProductViewSet()
    
#     # Call the instance method listt
#     value = obj.list(request=None)
#     # print(value)
    
#     data = json.loads(value)
#     print(data.data)
#     publish(data,"list_products")
#     print('Added a comment')

# channel.basic_consume(queue='admin', on_message_callback=callback, \
# auto_ack=True)

# print('Started Consuming')

# channel.start_consuming()

# channel.close()



def callback(ch, method, properties, body):
    print('Received in Django admin microservice')
    print("body",body)
    
    # Create an instance of ProductViewSet
    obj = ProductViewSet()
    
    # Call the instance method listt
    value = obj.list(request=None)
    # print(value)
    
  
    print("bbbbb",value.data)
    publish(body=value.data,method="list_products")
    print('Added a comment')

channel.basic_consume(queue='admin', on_message_callback=callback, \
auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()







