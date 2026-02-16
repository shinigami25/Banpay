# Frontend - Instrucciones de instalacion

SPA construida con **React 19**, **Vite**, **React Router DOM** y **Axios**.

## Requisitos previos

- [Node.js](https://nodejs.org/) (v18 o superior)
- npm (incluido con Node.js)
- La API debe estar corriendo en `http://localhost:8000` (ver instrucciones en la carpeta `api/`)

## Instalacion

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

## Build de produccion

```bash
npm run build
```

Los archivos generados quedan en la carpeta `dist/`.

Para previsualizar el build localmente:

```bash
npm run preview
```

## Paginas disponibles

| Ruta       | Descripcion              | Requiere login |
|------------|--------------------------|----------------|
| `/login`   | Inicio de sesion         | No             |
| `/users`   | CRUD de usuarios         | Si             |
| `/ghibli`  | Datos de Studio Ghibli   | Si             |

Cualquier ruta no definida redirige a `/login`.

## Credenciales por defecto

Usar las credenciales del usuario admin creado por la API:

- **Username**: `admin`
- **Password**: `admin`

## Estructura del proyecto

```
frontend/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── main.jsx              # Entry point
    ├── App.jsx               # Rutas y layout
    ├── api.js                # Cliente Axios con interceptor JWT
    ├── context/
    │   └── AuthContext.jsx   # Contexto de autenticacion (login, logout, token)
    └── pages/
        ├── LoginPage.jsx     # Formulario de login
        ├── UsersPage.jsx     # Gestion de usuarios
        └── GhibliPage.jsx    # Vista de datos Ghibli
```

## Scripts disponibles

| Comando         | Descripcion                              |
|-----------------|------------------------------------------|
| `npm run dev`   | Servidor de desarrollo con hot reload    |
| `npm run build` | Build optimizado para produccion         |
| `npm run preview` | Previsualizar el build de produccion   |
