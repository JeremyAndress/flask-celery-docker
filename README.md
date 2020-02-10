# Flask Celery

Este repositorio cuenta con una implementacion de flask y celery utilizando Factory Method Pattern. Creado como template para el futuro uso de proyectos que necesiten colas de tareas o tareas periodicas. 

## Dependencias 
Para hacer funcionar este template es necesario tener las siguientes herramientas instaladas en su maquina. Este template fue generado en un pc Linux, pero gracias al uso de Docker, su funcionamiento debe ser el mismo en maquinas Windows o Mac.

- [Docker] - version 19+
- [Docker Compose] - version 1.18+
- [Python] - version 3.5+

Si deseas conectar la aplicacion con una base de datos mysql sera necesario tener instalado algunos paquetes para el correcto funcionamiento con versiones python 3 en adelante, para instalarlas es necesario el siguiente comando :
```sh
$ sudo apt-get install python3-dev libmysqlclient-dev
```

## Como usar

- Primero debes clonar el repositorio, una vez en tu maquina situarte en la raiz de este.
- La primera modificacion que debes hacer es copiar el archivo .env.example donde se encuentran las variables de entorno, como .env para que puedan ser accesibles por docker. 

```sh
$ cp .env.example .env
```
- Luego debes crear las imagenes de docker, para esto usaremos docker-compose. Hay dos archivos local.yml (Destinado para ser utilizado en tu local, para probar el funcionamiento de tu codigo) y production.yml(Destinado para utilizar en un entorno productivo).El comando para contruir las imagenes es el siguiente:

```sh
$ docker-compose -f production.yml build
```
