# CVS Search - Frontend

Proyecto creado con [Create React App](https://github.com/facebook/create-react-app).

## Requisitos

Tener instalado [Node.js](https://nodejs.org/en/).

Revisar [instrucciones](https://nodejs.org/en/download/package-manager/) según el sistema operativo.

### **macOS y Windows**
Descargar el [instalador](https://nodejs.org/en/#home-downloadhead) directamente del [sitio principal](https://nodejs.org/en/).

### **Linux**

#### **Node.js v16.x:**

```
# Using Ubuntu

curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs

# Using Debian, as root

curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
apt-get install -y nodejs
```

Al momento de desarrollo de la app, la última versión de Node.js era la v14.17.4, y npm v6.14.14. Está bien si tenemos la versión más reciente.

## Instrucciones

Clonar o descargar el repositorio: `git clone https://192.168.50.141/prototypes/cvs_search`

Luego, dentro del directorio `/frontend` ejecutar el comando: `npm install`, que instalará las dependencias necesarias para ejecutar el proyecto.

Por último, ejecutar la app con el comando: `npm run`

Una nueva ventana del navegador debería abrirse con la dirección [http://localhost:3000](http://localhost:3000), o bien escribirla, para acceder a la app.

Ante cualquier cambio del código, el navegador refrescará el sitio.

## Endpoints

En este momento el endpoint que puede consumirse es el de `/search/elastic` (debe ejecutar el backend `elasticsearch_basic`).

El otro endpoint que puede ejecutarse es el de `/search/modelo`, pero hay que hacer un cambio en el `package.json` en la línea 25:

```json
"proxy": "http://localhost:${direccion donde corre model_apis}"
```

## Más información

Sobre crear una app de React con [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

Documentación de React: [React documentation](https://reactjs.org/).
