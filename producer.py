import pika
import json
import config as cfg

# Connect to RabbitMQ and create channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
channel = connection.channel()

json_file = open ('data.json')
json_array = json.load(json_file)
store_list = []

for item in json_array:

	message = json.dumps(item)

	# Send data
	channel.basic_publish(exchange='', routing_key=cfg.QUEUE_TOPIC, body=message)
	print(" [x] Sent data to RabbitMQ")

connection.close()
