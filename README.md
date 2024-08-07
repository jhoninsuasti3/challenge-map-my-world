# Challenge Map my world

# Proyecto hecho con FASTAPI

## Installation

Para empezar a trabajar el proyecto las configuraciones iniciales del entorno, esto no será necesario despues de construida la imagen docker del proyecto

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt`
```

## Docker: Run Project

### Run container

```
docker-compose up --force-recreate --build
```

# Creacion de accesos
En la raiz del proSe debe crear un archivo .env y colocar los datos
DB_HOST=db
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_PORT=5432

# Validaciones despliegue

Una vez haya corrido docker-compose up --force-recreate --build, se debe validar las apis a traves de 
http://localhost:8001/docs#/  La documentacion y pruebas de la misma será en swagger
http://localhost:5001/browser/  La base de datos se despliega aquí, para ello considerar asociar los del archivo .env :

port: 5432 (Es importante no contar con el puerto usado en la maquina que se probará la solución)


# Instructions to use



### Run tests

```
Terminal 1:
docker-compose up

Terminal 2:
docker-compose exec api bash
python -m pytest
```

---


## Run pre-commit

pre-commit run --all-files

## Docker-compose validate coverage

docker-compose -f docker-compose.testing.yml up --force-recreate --build
docker-compose -f docker-compose.testing.yml run --rm api-total sh -c "pytest -vv"
