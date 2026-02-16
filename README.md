# Users API - Instrucciones de instalacion

API REST construida con **FastAPI**, **PostgreSQL**, **SQLAlchemy** y **JWT** para autenticacion.

## Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/)
- (Opcional) Python 3.14+ si se quiere ejecutar sin Docker

## Levantar con Docker (recomendado)

```bash
docker compose up --build
```

Esto levanta dos servicios:

| Servicio | Puerto | Descripcion                        |
|----------|--------|------------------------------------|
| `api`    | 8000   | FastAPI + Uvicorn                  |
| `db`     | 5432   | PostgreSQL 17 (alpine)             |


## Requisitos previos

- [Node.js](https://nodejs.org/) (v18 o superior)
- npm (incluido con Node.js)
- La API debe estar corriendo en `http://localhost:8000` (ver instrucciones en la carpeta `api/`)

## Instalacion Front

```bash
cd frontend
npm install
```

## Levantar en modo desarrollo

```bash
npm run dev
```

El servidor de desarrollo se levanta por defecto en **http://localhost:5173**.

Vite esta configurado con un proxy que redirige todas las peticiones `/api/*` hacia `http://localhost:8000`, por lo que no hay problemas de CORS en desarrollo.

usuario precargado : admin admin
