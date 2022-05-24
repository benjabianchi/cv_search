from flask import Flask
from flask import jsonify
from flask import Flask , jsonify , request
from search_cvs import model_prediction
import pickle
from flask_cors import CORS

app= Flask("__name__")
CORS(app)

global bag_of_words
global vectorizer

bag_of_words = None
vectorizer = None

def threshold(value,cv):
    filter_cv = []
    for i in cv:
        if round(float(i[1]),3) < value:

            filter_cv.append(i)

    return {"cv":filter_cv}


def reload():
    try:
      with open('model/bow.pkl', 'rb') as f:
         bag_of_words = pickle.load(f)

      with open('model/vectorizer.pkl', 'rb') as f:
         vectorizer = pickle.load(f)
      return bag_of_words,vectorizer
    except OSError:
      print("No hay ningun archivo para cargar! Debes re-entrenar el modelo y usar reload.")

@app.route('/reload',methods=["GET"])
def index1():
    if request.method == "GET":
        reload()
    return jsonify({"cv":"Modelo Recargado"})

@app.route('/search',methods=["POST"])
def index():
    if request.method == "POST":
        content = request.get_json()
        sentence = content["key"]
        limit = content["limit"]
        threshold_ = content["threshold"]
        response = model_prediction(str(sentence),int(limit),bag_of_words,vectorizer)
        print("Test...___")
        response = threshold(float(threshold_),response)

    return jsonify(response)


if __name__ == "__main__":
  bag_of_words,vectorizer = reload()
  app.run(host="0.0.0.0",port=4000,debug=True)
