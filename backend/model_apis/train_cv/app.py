from flask import Flask
from flask import jsonify
from flask import Flask , jsonify , request
from retrain_model import retrain
from flask_cors import CORS

app= Flask("__name__")
CORS(app)
@app.route('/retrain',methods=["GET"])
def index():
    if request.method == "GET":
        retrain("cvs/")

    return jsonify({"CV's":"modelo re-entrenado"})


if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000,debug=True)
