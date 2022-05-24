from flask import Flask
from flask import jsonify
from flask import Flask , jsonify , request
import uuid
from os import walk
import paho.mqtt.client as mqtt
broker = "mqtt"
port = 1883

app= Flask("__name__")
# client = mqtt.Client()
# client.connect(broker)
# es = Elasticsearch(['elasticsearch'],
#     scheme="http",
#     port=9200)

#print("ESTA FUNCIONANDO!")

# @app.route('/bulk_csv',methods=["GET"])
# def index1():
#     if request.method == "GET":
#         if es.indices.exists(index="cvs_index"):
#             es.delete_by_query(index="cvs_index", body={"query": {"match_all": {}}})

#             message = "CSV Actualizado"

#         else:
#             es.indices.create(index="cvs_index")

#             message = "El indice no existe, hemos creado uno con exito!"
#         with open('csv/CVs.csv',encoding="utf8") as f:
#             reader = csv.DictReader(f)
#             helpers.bulk(es, reader, index="cvs_index")
#     return jsonify({"message":message})

# @app.route('/test',methods=["GET"])
# def index3():
#     if request.method == "GET":
#         if es.indices.exists(index="cvs_index"):
#             print("Existe")

#         else:
#             print("No existe, debes crear el indice primero!")

#     return jsonify({"message":message})


# @app.route('/create_csv',methods=["GET"])
# def index2():
#     if request.method == "GET":
#         create_csv("cvs_ejemplo/")
#     return jsonify({"create_csv":"OK"})


## Endpoint para mandar mensaje para hacer el bulk
@app.route('/bulk_csv',methods=["GET"])
def index():
    if request.method == "GET":
        uuid_id = uuid.uuid4()
        response = {"id":uuid_id,"command":"load_csv_elastic"}
        client.publish("commands/elastic",str(response))
    return jsonify({"action":"OK"})


## Endpoint para mandar mensaje para recargar el modelo
@app.route('/reload_csv',methods=["GET"])
def index1():
    if request.method == "GET":
        uuid_id = uuid.uuid4()
        response = {"id":uuid_id,"command":"generate_csv"}
        client.publish("commands/elastic",str(response))
    return jsonify({"action":"OK"})


if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000,debug=True)
