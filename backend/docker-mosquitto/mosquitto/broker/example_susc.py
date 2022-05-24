import paho.mqtt.client as mqtt
from random import randrange
import time


def on_message(client,userdata,message):
    #data = eval(str(message.payload))
    print(message.topic)
    if message.topic == "commands/reload":
        data = eval(message.payload)
        ## Pedir que se haga el reload del modelo
        print(f"El usuario quiere recargar el modelo y su id es {data['id']}")
    elif message.topic == "commands/retrain":
        data = eval(message.payload)
        ## Pedir que se haga el retrain del modelo
        print(f"El usuario quiere re-entrenar el modelo y su id es {data['id']}")

client = mqtt.Client()

client.connect("mqtt")

client.subscribe("commands/#")

client.on_message = on_message

print("Esperando data...")

client.loop_forever()
