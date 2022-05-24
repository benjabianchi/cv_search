import paho.mqtt.client as mqtt
from random import randrange
import time
from externalFuncs import create_csv
from elasticsearch import helpers, Elasticsearch


es = Elasticsearch(['elasticsearch'],
     scheme="http",
     port=9200)

## mandar por mensaje el metodo que queremos implementar(bulk_cvs o reload) (HECHO)

## cambiar nombre de las varialbes bulk y reload (que sean mas explicitos load_csv_elastic & generate_csv)
def on_message(client,userdata,message):
    #data = eval(str(message.payload))
    print(message.topic)
    if eval(message.payload)["command"] == "load_csv_elastic":
        try:
            data = eval(message.payload)
            ## Pedir que haga el bulk a elastic search
            if es.indices.exists(index="cvs_index"):
                es.delete_by_query(index="cvs_index", body={"query": {"match_all": {}}})



            else:
                es.indices.create(index="cvs_index")

                message = "El indice no existe, hemos creado uno con exito!"
            with open('csv/CVs.csv',encoding="utf8") as f:
                reader = csv.DictReader(f)
                helpers.bulk(es, reader, index="cvs_index")
            client.publish("commands/message",str({"status":"Done","id":data["id"],"operation":"load_csv_elastic"})
        except Exception as e:
            client.publish("commands/message",str({"status":"ERROR","id":data["id"],"operation":"load_csv_elastic"}))

    elif eval(message.payload)["command"] == "generate_csv":
        try:
            data = eval(message.payload)
            ## Pedir que se recargue el csv
            create_csv("cvs_ejemplo/")
            print(f"ID del Reload: {data['id']}")
            ## Publicar que temrino la tarea con ID. elastic/message
            ## ENVIAR ID Y ESTADO
            client.publish("commands/message",str({"status":"Done","id":data["id"],"operation":"generate_csv"}))
            ## MANEJO DE EXCEPECIONES Y ERRORES
        except Exception as e:
            client.publish("commands/message",str({"status":"ERROR","id":data["id"],"operation":"generate_csv"}))


client = mqtt.Client()

client.connect("mqtt",1883)

client.subscribe("commands/elastic")

client.on_message = on_message

print("Esperando data...")

client.loop_forever()
