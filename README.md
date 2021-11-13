# Tienda la 40 - Orquestador
Repositorio para el orquestador (back-end) del proyecto de tienda de barrio "Tienda La 40" con fines académicos para Ingeniería de Software 1 de la MCIC de la Universidad Distrital Francisco José de Caldas, Bogotá, Colombia.

## Integrantes

- Javier Hospital Melo
- Norbey Danilo Muñoz
- Camilo Enrique Rocha
- Juan Sebastián Sánchez
- Brayan Leonardo Sierra
- Ivan Daniel Villegas

## Especificaciones Técnicas
### Tecnologías Implementadas y Versiones

- Flask 0.12, SQLAlquemy 2.5.1
- Python 3.6
- Sqlite 3
- Docker

### Microservices

Esta aplicación trabaja una arquitectura de microservicios. 

```
.
├── apicrud (crud api operations: GET, POST, PATCH, DELETE, GET BY ID)
    ├── database
        ├── tienda.db (database sqlite3)
        └── tienda.sql (script)
    ├── app.py
    ├── requirements.txt
    ├── controller.py (crud operations)
    ├── models.py (classes-models)
    ├── serialisers.py (helps data transformation)
    └── Dockerfile
├── cantidad (microservice)
    ├── app.py (consume apicrud)
    ├── requirements.txt
    └── Dockerfile
├── carrito (microservice)
    └── ...
├── clientes (microservice)
    └── ...
├── productos (microservice)
    └── ...
├── docker-compose.yml
└── nginx.conf (NGINX as an API Gateway)
```

#### NGINX as an API Gateway
<strong><em>"As the leading high‑performance, lightweight reverse proxy and load balancer, NGINX has the advanced HTTP processing capabilities needed for handling API traffic. This makes NGINX the ideal platform with which to build an API gateway" *[NGINX as an API Gateway](https://www.nginx.com/blog/deploying-nginx-plus-as-an-api-gateway-part-1/)*</em></strong>

Este proyecto emplea NGINX como API GATEWAY para manejar el tráfico. La estructura referencia es tomada de *[NGINX as an API Gateway](https://www.nginx.com/blog/deploying-nginx-plus-as-an-api-gateway-part-1/)* y es como la imagen abajo:

![image](https://user-images.githubusercontent.com/24207969/141644322-bb0159e1-0f2f-424e-a38e-f3565bc675e5.png)

Donde los *services* hacen referencia a nuestros microservicios antes mencionados en la estructura (cliente, productos, etc)

### Ejecución del Proyecto / Instrucciones

```
# 1. Obtener el repositorio de git
git clone https://github.com/Ataches/TiendaLa40_Orquestador.git

# 2. Moverse a la carpeta del repositorio, si aplica
cd TiendaLa40_Orquestador

# 3. Moverse a la rama **master**
git pull origin master && git checkout master

# 4. Instalar dependencias

# 5. Ejecutar
docker-compose build
docker-compose run
docker-compose up 
docker-compose up -d
```

### Licencia

This file is part of TiendaLa40_Orquestador.

TiendaLa40_Orquestador is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

TiendaLa40_Orquestador is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with sintomas_crud. If not, see https://www.gnu.org/licenses/.
