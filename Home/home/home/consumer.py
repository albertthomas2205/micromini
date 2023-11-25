import pika

params = pika.URLParameters("amqps://qmcvlsmb:vEbAOOExvR7RH2y-zhE3K4PdVzdc1etx@puffin.rmq2.cloudamqp.com/qmcvlsmb")

connection = pika.BlockingConnection(params)
channel = connection.channel()

try:
    channel.queue_declare(queue='admin')
except pika.exceptions.ChannelClosed as e:
    print(f"Error declaring queue: {e}")

def callback(ch, method, properties, body):
    print("received in admin")
    print(body)

if __name__ == "__main__":
    try:
        channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
        print("started consuming")
        channel.start_consuming()
    except pika.exceptions.ConnectionClosed as e:
        print(f"Error connecting to RabbitMQ: {e}")
