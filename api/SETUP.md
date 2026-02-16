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

Al iniciar, el contenedor de la API ejecuta automáticamente:
1. Las migraciones de Alembic (`alembic upgrade head`)
2. Un seed que crea el usuario admin por defecto

Para correr en segundo plano:

```bash
docker compose up --build -d
```

Para detener los servicios:

```bash
docker compose down
```

Para detener y eliminar los volúmenes (borra la base de datos):

```bash
docker compose down -v
```

## Levantar sin Docker (desarrollo local)

### 1. Crear y activar un entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

El archivo `.env` en la raíz del proyecto contiene la configuración necesaria:

| Variable                      | Descripcion                  | Default                                |
|-------------------------------|------------------------------|----------------------------------------|
| `DB_HOST`                     | Host de PostgreSQL           | `localhost`                            |
| `DB_PORT`                     | Puerto de PostgreSQL         | `5432`                                 |
| `DB_NAME`                     | Nombre de la base de datos   | `USER_SERVICE`                         |
| `DB_USER`                     | Usuario de PostgreSQL        | `postgres`                             |
| `DB_PASSWORD`                 | Contraseña de PostgreSQL     | `postgres123`                          |
| `JWT_SECRET_KEY`              | Clave secreta para JWT       | `super-secret-key-change-in-production`|
| `JWT_ALGORITHM`               | Algoritmo JWT                | `HS256`                                |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Expiración del access token  | `30`                                   |
| `REFRESH_TOKEN_EXPIRE_DAYS`   | Expiración del refresh token | `7`                                    |

### 4. Tener PostgreSQL corriendo

Asegurarse de tener una instancia de PostgreSQL accesible con la base de datos `USER_SERVICE` creada.

### 5. Ejecutar migraciones

```bash
cd src
alembic upgrade head
```

### 6. Iniciar el servidor

```bash
cd src
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Verificar que funciona

Una vez levantada la API, acceder a:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Endpoints disponibles

### Auth (`/api/auth`)
| Método | Ruta       | Descripción                    | Auth |
|--------|------------|--------------------------------|------|
| POST   | `/login`   | Iniciar sesión (obtener token) | No   |
| POST   | `/refresh` | Refrescar access token         | No   |

### Users (`/api/users`)
| Método | Ruta          | Descripción          | Auth |
|--------|---------------|----------------------|------|
| GET    | `/`           | Listar usuarios      | Si   |
| GET    | `/{user_id}`  | Obtener usuario      | Si   |
| POST   | `/`           | Crear usuario        | No   |
| PUT    | `/{user_id}`  | Actualizar usuario   | Si   |
| DELETE | `/{user_id}`  | Eliminar usuario     | Si   |

### Ghibli (`/api/ghibli`)
| Método | Ruta | Descripción           | Auth |
|--------|------|-----------------------|------|
| GET    | `/`  | Obtener datos Ghibli  | Si   |

## Usuario admin por defecto

Al iniciar la API se crea automaticamente un usuario administrador:

- **Username**: `admin`
- **Password**: `admin`

## Estructura del proyecto

```
api/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── src/
    ├── main.py
    ├── alembic/              # Migraciones de base de datos
    ├── application/
    │   ├── schemas/          # DTOs (Pydantic)
    │   └── services/         # Lógica de negocio
    ├── domain/
    │   ├── entities/         # Modelos de dominio (SQLAlchemy)
    │   ├── enums/            # Enumeraciones
    │   └── repositories/     # Interfaces de repositorio
    ├── infrastructure/
    │   ├── database.py       # Configuración de BD
    │   ├── http/             # Clientes HTTP externos
    │   ├── repositories/     # Implementaciones de repositorio
    │   └── security/         # JWT y hashing de passwords
    ├── presentation/
    │   └── routers/          # Endpoints de la API
    └── setup/
        └── dependencies.py   # Inyección de dependencias
```
