# Backend del proyecto (API y Modelos)

## elasticsearch_basic
Este folder tiene un modelo con elastic search para cargar los CV's y realizar querys mediante la API de elastic.

## elasticsearch_model
Este folder tiene el modelo de elastic completo, con las API's personalizadas y MQTT (brokers y API para mandar mensajes).

## model_apis
Este folder contiene el modelo ad-hoc que utiliza distancias para calcular similitud entre CV's. Podemos encontrar tanto el entrenamiento como la busqueda.


## Instalacion

Primero debe tener instalado docker dentro de su computadora:

[Windows y Mac](https://geekflare.com/es/docker-desktop/)

[Ubuntu](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04)

### Ya instalado puede utilizarlo para correr los modelos

Ubicarse en la folder del modelo que quiere correr y correr el docker compose con el siguiente comando:
```bash
docker-compose up
```
## Endpoints de cada modelo

## model_apis

### API Search CV

``` enpoint/reload – GET ```

Esta petición simplemente recarga el modelo en disco devuelve un json con la siguiente confirmación.
{“cv”:”Modelo Recargado”}

``` endpoint/search - POST ```

Esta petición es la encargada de recibir los datos de la posición(eg: “Python Java Hadoop”) y devuelve un Json con los CV’s mas adecuado para dicha posición. El parámetro “key” es la oración con las tecnologías buscadas y el limit es el número máximo de CV’s que queremos recibir. También se agrego el parámetro threshold el cual es un umbral que nos permite hacer búsquedas mas precisas, mientras mas chico el valor mas exigente será la búsqueda.

Input: ``` {"key":"java python","limit":"5","threshold":1} ```

Output:
```bash
{
    "cv": [
        [
            "cvs/AdrianGrebin.pdf",
            0.8
        ],
        [
            "cvs/Alberto Andria.pdf",
            0.8321
        ],
        [
            "cvs/Alberto Eduardo.pdf",
            0.8575
        ],
        [
            "cvs/Alan Vaudagna.pdf",
            0.8944
        ],
        [
            "cvs/21595_POZO--ANDRES-2016-11-01.pdf",
            0.9191
        ]
    ]
}

```


### API Retrain CV

``` enpoint/retrain – GET ```

Este petición se utiliza para re-entrenar el “modelo”, simplemente devuelve un mensaje de confirmación en forma de json. Cuando termine el proceso de re-entrenamiento lanza el mensaje( el proceso puede tomarse un tiempo dependiendo de la cantidad de CV que existan)

``` {"CV's":"modelo re-entrenado"} ```

## Modelo ElasticSearch Basico

Este es un método básico que solamente nos permite hacer querys a elasticsearch de manera aislada. Es útil para testear querys sin necesidad de tener otros componentes, ya que elastic nos viene con una API por defecto para hacer querys.

Primero seria conveniente tener instalado Anaconda para poder utilizar jupyter y probar querys alli.

[Anaconda Instalacion](https://www.anaconda.com/products/individual)

Al tener Anaconda instalado podemos simplemente lanzar jupyter notebook en la misma ubicacion donde esta el notebook (.ipynb).

Antes debemos lanzar el docker-compose que esta ubicado en *backend/elastic_basic*, esto nos instalara elastic en un contenedor y seremos capaces de agregar indexar datos y hacer consultas.

Para levantarlo usar:

```bash
docker-compose up
```

Al ya tener corriendo el contenedor podemos acceder a el y para eso usaremos el notebook. Primero debemos instalar la libreria de Python para usar elastic search desde Python.

```python
!pip install elasticsearch
```

Ya instalado podemos conectarnos a elastic usando este comando.

```python
from elasticsearch import helpers, Elasticsearch
import csv
es = Elasticsearch(HOST="http://localhost", PORT=9200)
```

Luego ya podemos indexar (agregar datos) datos a un indice utilizando este codigo.

```python
with open('CVS.csv',encoding="utf8") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='cvs_index')
```

Listo ya tendriamos nuestros datos de los CVS vinculados al indice, ahora podremos hacer querys sobre esos datos.
```python
result = es.search(index="cvs_index", body={"_source":["path"],
"query": {
"bool" : {
"must" : [

 {
"match": {
"words": "java"
}
},
{
"match": {
"words": "python"
}
},
 {
"match": {
"local": "Cordoba"
}
}
]

}
}

})
```

Y mediante este comando podemos ver los resultados de la query:


```python
result["hits"]["hits"]
```

## Modelo Elastic Search Completo

Este modelo contiene Elastic Search, API's y mqtt. La  API manda mensajes a los topicos de Mqtt y estos disparan acciones como puede ser el load de CV's a elastic o generar un csv nuevo. Esta API se encuentra dentro del folder elastic_model/app.

Luego en el folder elastic_model/broker encontramos los procesos de generar csv y cargar a elastic. Tambien dentro del script example_susc.py podemos ver la iniciación del broker mqtt junto con los topicos indicados (en este caso al commands/elastic).

Cada parte esta dockerizada y para lanzar en conjunto el modelo se debe utilizar docker compose.

Con el siguiente comando se levanta el modelo completo.

```bash
docker-compose up
```
