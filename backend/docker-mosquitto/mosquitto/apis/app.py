from flask import Flask
from flask import jsonify
from flask import Flask , jsonify , request
import paho.mqtt.client as mqtt
import uuid

app= Flask("__name__")

client = mqtt.Client()
client.connect("mqtt",port=1883,keepalive=60)

## Endpoint para mandar mensaje para re-entrenar
@app.route('/retrain',methods=["GET"])
def index():
    if request.method == "GET":
        uuid_id = uuid.uuid4()
        response = {"id":uuid_id}
        client.publish("commands/retrain",str(response))
    return jsonify({"action":"OK"})


## Endpoint para mandar mensaje para recargar el modelo
@app.route('/reload',methods=["GET"])
def index1():
    if request.method == "GET":
        uuid_id = uuid.uuid4()
        response = {"id":uuid_id}
        client.publish("commands/reload",str(response))
    return jsonify({"action":"OK"})

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000,debug=True)
