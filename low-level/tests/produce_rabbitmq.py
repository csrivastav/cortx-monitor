#!/usr/bin/env python
import pika
import socket

creds = pika.PlainCredentials('sspluser', 'sspl4ever')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', virtual_host='SSPL', credentials=creds))
channel = connection.channel()

channel.exchange_declare(exchange='sspl_bcast',
                         type='topic', durable=True)

result = channel.queue_declare(exclusive=False)
channel.queue_bind(exchange='sspl_bcast',
                   queue='SSPL-LL')

msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

jsonMsg="Hello World!" 
channel.basic_publish(exchange='sspl_bcast',
                      routing_key='sspl_ll',
                      properties=msg_props, 
                      body=str(jsonMsg))             

print "Successfully Sent: %s" % jsonMsg

connection.close()
del(connection)




