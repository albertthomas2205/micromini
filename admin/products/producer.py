import pika, json

params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    # print(method,body)
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', \
    body=json.dumps(body), properties=properties) 
    # routing key here must match the queue name in the consumer\
    # of the flask app
# import pika

# params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

# connection = pika.BlockingConnection(params)
# channel = connection.channel()

# def publish():
#     print("haiiiii")
#     channel.basic_publish(exchange='', routing_key='admin', body='hello albert')

# if __name__ == "__main__":
#     publish()
#     connection.close()
# your_app/tasks.py
# from celery import shared_task
# import pika

# @shared_task
# def publish(data):
    
#     try:
#         params = pika.URLParameters("amqp://guest:guest@localhost:5672/")
#         connection = pika.BlockingConnection(params)
#         channel = connection.channel()

#         channel.queue_declare(queue='your_queue_name')
#         channel.basic_publish(exchange='', routing_key='your_queue_name', body=data)

#         connection.close()
#     except Exception as e:
#         print(f"Error sending message to RabbitMQ: {str(e)}")

# import pika

# def publish(message):
#     # Define connection parameters
#     params = pika.URLParameters("amqp://guest:guest@localhost:5672/")

#     # Establish connection to RabbitMQ server
#     connection = pika.BlockingConnection(params)

#     # Open a channel on the connection
#     channel = connection.channel()

#     # Declare the queue if it doesn't already exist
#     channel.queue_declare(queue='admin', durable=True)

#     # Send the message to the queue
#     channel.basic_publish(exchange='', routing_key='admin', body=message)

#     # Close the connection
#     connection.close()

# # Example usage

