FROM openjdk:slim
COPY --from=python:3.6 / /

 WORKDIR /app

 COPY requirements.txt retrain_model.py app.py /app

 RUN pip install -r requirements.txt

 WORKDIR /app/cvs

 COPY /cvs_ejemplo/ /app/cvs

 WORKDIR /app

 CMD ["python3" , "app.py"]
