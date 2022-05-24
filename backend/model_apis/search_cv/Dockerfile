 FROM python:3.7

 WORKDIR /app

 # COPY requirements.txt search_cvs.py app.py /app

 RUN pip install -r requirements.txt

 WORKDIR /app/cvs

 # COPY /cvs_ejemplo/ /app/cvs

 # COPY /model/ /app/model

 WORKDIR /app

 CMD ["python3" , "app.py"]
