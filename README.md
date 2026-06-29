# Fútbol Stats API

API REST para la gestión de estadísticas de fútbol: jugadores, partidos, métricas técnicas y tácticas, scouting, salud y más.

---

## Integrantes

- Edison Ludena
- Danna González
- Santiago Colimba

---

## Descripción del sistema

Fútbol Stats API es un backend desarrollado con **Django REST Framework** que permite a entidades deportivas (clubes, academias) gestionar información completa de sus jugadores y cuerpo técnico. El sistema ofrece:

- Autenticación segura con **JWT** (access + refresh tokens)
- Roles de usuario: **Coach**, **Scout** y **Player**
- CRUD completo de jugadores, partidos, alineaciones y eventos en vivo
- Módulo de scouting con reportes, métricas técnicas y tácticas
- Seguimiento de salud, antropometría, lesiones, rehabilitación y dietas
- Contratos internos y valoración económica de jugadores
- Despliegue en producción con **Gunicorn + Nginx** en Azure

---

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/EdisonLudena/backend_proyecto_integrador_futbol.git
cd backend_proyecto_integrador_futbol
```

### 2. Crear el entorno virtual con uv

```bash
pip install uv
uv venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias

```bash
uv sync
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
nano .env
```

Contenido mínimo del `.env`:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=futbol_db
DB_USER=futbol_user
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Ejecutar migraciones

```bash
uv run python manage.py migrate
```

### 6. Crear superusuario

```bash
uv run python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
uv run python manage.py runserver
```

La API estará disponible en `http://localhost:8000/api/`

---

## Despliegue en producción (Azure VM)

### Requisitos previos

- VM Ubuntu 22.04 en Azure
- Puerto 80 abierto en el Network Security Group

### 1. Configuración del VPS

```bash
# Crear usuario del sistema
sudo adduser futbol
sudo usermod -aG www-data futbol

# Clonar el proyecto
sudo mkdir -p /opt/futbol
sudo chown futbol:www-data /opt/futbol
cd /opt/futbol
git clone https://github.com/EdisonLudena/backend_proyecto_integrador_futbol.git .

# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv sync
```

### 2. Configuración de PostgreSQL

```bash
sudo apt install -y postgresql postgresql-contrib
sudo -u postgres psql

-- En psql:
CREATE DATABASE futbol_db;
CREATE USER futbol_user WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE futbol_db TO futbol_user;
\q
```

### 3. Configuración de Gunicorn

Crear `/etc/systemd/system/gunicorn-futbol.service`:

```ini
[Unit]
Description=Gunicorn daemon for FutbolAPI
After=network.target postgresql.service

[Service]
User=futbol
Group=www-data
WorkingDirectory=/opt/futbol
RuntimeDirectory=gunicorn-futbol
Environment="PATH=/opt/futbol/.venv/bin"
EnvironmentFile=/opt/futbol/.env
ExecStart=/opt/futbol/.venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/run/gunicorn-futbol/gunicorn.sock \
          --access-logfile /var/log/gunicorn-futbol-access.log \
          --error-logfile /var/log/gunicorn-futbol-error.log \
          config.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn-futbol
sudo systemctl enable gunicorn-futbol
```

### 4. Configuración de Nginx

```bash
sudo apt install -y nginx
```

Crear `/etc/nginx/sites-available/futbol`:

```nginx
server {
    listen 80;
    server_name TU_IP_PUBLICA;

    location /static/ {
        alias /opt/futbol/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn-futbol/gunicorn.sock;
        proxy_read_timeout 90;
        proxy_connect_timeout 90;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/futbol /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
```

---

## Uso de la API

### Obtención de token JWT

```bash
POST /api/auth/login/

{
  "email": "coach@futbol.com",
  "password": "Coach1234!"
}
```

Respuesta:

```json
{
  "access": "eyJ...",
  "refresh": "eyJ..."
}
```

### Uso de endpoints protegidos

Incluye el token en el header de cada petición:

```
Authorization: Bearer eyJ...
```

### Ejemplos de peticiones

**Registrar usuario:**
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "coach@futbol.com", "password": "Coach1234!", "nombre_completo": "Carlos Pérez", "tipo_usuario": "Coach"}'
```

**Listar jugadores:**
```bash
curl http://localhost:8000/api/jugadores/ \
  -H "Authorization: Bearer TU_ACCESS_TOKEN"
```

**Crear jugador:**
```bash
curl -X POST http://localhost:8000/api/jugadores/ \
  -H "Authorization: Bearer TU_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entidad": "UUID_ENTIDAD",
    "nombres": "Luis Miguel",
    "apellidos": "Torres",
    "fecha_nacimiento": "2000-03-15",
    "pie_dominante": "Derecho"
  }'
```

**Refrescar token:**
```bash
curl -X POST http://localhost:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "TU_REFRESH_TOKEN"}'
```

---

## Endpoints

Todos los endpoints usan el prefijo `/api/`. Los endpoints protegidos requieren el header `Authorization: Bearer <token>`.

### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/health/` | Estado del servidor |
| `POST` | `/api/auth/register/` | Registrar usuario |
| `POST` | `/api/auth/login/` | Iniciar sesión |
| `POST` | `/api/auth/logout/` | Cerrar sesión |
| `POST` | `/api/auth/token/refresh/` | Refrescar access token |
| `POST` | `/api/auth/token/verify/` | Verificar token |

### Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/users/` | Listar usuarios |
| `GET` | `/api/users/{id}/` | Detalle de usuario |
| `PATCH` | `/api/users/{id}/` | Actualizar usuario |
| `DELETE` | `/api/users/{id}/` | Eliminar usuario |

### Suscripciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/suscripciones/` | Crear suscripción |
| `GET` | `/api/suscripciones/` | Listar suscripciones |
| `GET` | `/api/suscripciones/{id}/` | Detalle de suscripción |
| `PATCH` | `/api/suscripciones/{id}/` | Actualizar suscripción |
| `DELETE` | `/api/suscripciones/{id}/` | Eliminar suscripción |

### 🏟️ Entidades

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/entidades/` | Crear entidad |
| `GET` | `/api/entidades/` | Listar entidades |
| `GET` | `/api/entidades/{id}/` | Detalle de entidad |
| `PUT` | `/api/entidades/{id}/` | Actualizar entidad |
| `DELETE` | `/api/entidades/{id}/` | Eliminar entidad |

### Sedes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/sedes/` | Crear sede |
| `GET` | `/api/sedes/` | Listar sedes |
| `GET` | `/api/sedes/{id}/` | Detalle de sede |
| `PATCH` | `/api/sedes/{id}/` | Actualizar sede |
| `DELETE` | `/api/sedes/{id}/` | Eliminar sede |

### Categorías

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/categorias/` | Crear categoría |
| `GET` | `/api/categorias/` | Listar categorías |
| `GET` | `/api/categorias/{id}/` | Detalle de categoría |
| `PATCH` | `/api/categorias/{id}/` | Actualizar categoría |
| `DELETE` | `/api/categorias/{id}/` | Eliminar categoría |

### Posiciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/posiciones/` | Crear posición |
| `GET` | `/api/posiciones/` | Listar posiciones |
| `GET` | `/api/posiciones/{id}/` | Detalle de posición |
| `PATCH` | `/api/posiciones/{id}/` | Actualizar posición |
| `DELETE` | `/api/posiciones/{id}/` | Eliminar posición |

### Jugadores

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/jugadores/` | Crear jugador |
| `GET` | `/api/jugadores/` | Listar jugadores |
| `GET` | `/api/jugadores/{id}/` | Detalle de jugador |
| `PATCH` | `/api/jugadores/{id}/` | Actualizar jugador |
| `DELETE` | `/api/jugadores/{id}/` | Eliminar jugador |

### Jugador-Posiciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/jugador-posiciones/` | Asignar posición a jugador |
| `GET` | `/api/jugador-posiciones/` | Listar relaciones |

### Representantes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/representantes/` | Crear representante |
| `GET` | `/api/representantes/` | Listar representantes |
| `GET` | `/api/representantes/{id}/` | Detalle de representante |
| `PATCH` | `/api/representantes/{id}/` | Actualizar representante |
| `DELETE` | `/api/representantes/{id}/` | Eliminar representante |

### Prospectos Scouting

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/prospectos-seguimiento/` | Crear prospecto |
| `GET` | `/api/prospectos-seguimiento/` | Listar prospectos |
| `GET` | `/api/prospectos-seguimiento/{id}/` | Detalle de prospecto |
| `PATCH` | `/api/prospectos-seguimiento/{id}/` | Actualizar prospecto |
| `DELETE` | `/api/prospectos-seguimiento/{id}/` | Eliminar prospecto |

### Reportes Scouting

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/reportes-scouting/` | Crear reporte |
| `GET` | `/api/reportes-scouting/` | Listar reportes |
| `GET` | `/api/reportes-scouting/{id}/` | Detalle de reporte |
| `PATCH` | `/api/reportes-scouting/{id}/` | Actualizar reporte |
| `DELETE` | `/api/reportes-scouting/{id}/` | Eliminar reporte |

### Métricas Técnicas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/metricas-tecnicas/` | Crear métrica técnica |
| `GET` | `/api/metricas-tecnicas/` | Listar métricas técnicas |
| `GET` | `/api/metricas-tecnicas/{id}/` | Detalle de métrica |
| `PATCH` | `/api/metricas-tecnicas/{id}/` | Actualizar métrica |
| `DELETE` | `/api/metricas-tecnicas/{id}/` | Eliminar métrica |

### Métricas Tácticas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/metricas-tacticas/` | Crear métrica táctica |
| `GET` | `/api/metricas-tacticas/` | Listar métricas tácticas |
| `GET` | `/api/metricas-tacticas/{id}/` | Detalle de métrica |
| `PATCH` | `/api/metricas-tacticas/{id}/` | Actualizar métrica |
| `DELETE` | `/api/metricas-tacticas/{id}/` | Eliminar métrica |

### Valoración Económica

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/valoracion-economica/` | Crear valoración |
| `GET` | `/api/valoracion-economica/` | Listar valoraciones |
| `GET` | `/api/valoracion-economica/{id}/` | Detalle de valoración |
| `PATCH` | `/api/valoracion-economica/{id}/` | Actualizar valoración |
| `DELETE` | `/api/valoracion-economica/{id}/` | Eliminar valoración |

### Partidos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/partidos/` | Crear partido |
| `GET` | `/api/partidos/` | Listar partidos |
| `GET` | `/api/partidos/{id}/` | Detalle de partido |
| `PATCH` | `/api/partidos/{id}/` | Actualizar partido |
| `DELETE` | `/api/partidos/{id}/` | Eliminar partido |

### Alineaciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/alineaciones/` | Crear alineación |
| `GET` | `/api/alineaciones/` | Listar alineaciones |
| `GET` | `/api/alineaciones/{id}/` | Detalle de alineación |
| `PATCH` | `/api/alineaciones/{id}/` | Actualizar alineación |
| `DELETE` | `/api/alineaciones/{id}/` | Eliminar alineación |

### Eventos Live

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/eventos-live/` | Crear evento |
| `GET` | `/api/eventos-live/` | Listar eventos |
| `GET` | `/api/eventos-live/{id}/` | Detalle de evento |
| `PATCH` | `/api/eventos-live/{id}/` | Actualizar evento |
| `DELETE` | `/api/eventos-live/{id}/` | Eliminar evento |

### Evaluación Post-Partido

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/evaluacion-post-partido/` | Crear evaluación |
| `GET` | `/api/evaluacion-post-partido/` | Listar evaluaciones |
| `GET` | `/api/evaluacion-post-partido/{id}/` | Detalle de evaluación |
| `PATCH` | `/api/evaluacion-post-partido/{id}/` | Actualizar evaluación |
| `DELETE` | `/api/evaluacion-post-partido/{id}/` | Eliminar evaluación |

### Contratos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/contratos/` | Crear contrato |
| `GET` | `/api/contratos/` | Listar contratos |
| `GET` | `/api/contratos/{id}/` | Detalle de contrato |
| `PATCH` | `/api/contratos/{id}/` | Actualizar contrato |
| `DELETE` | `/api/contratos/{id}/` | Eliminar contrato |

### Salud

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/salud/` | Crear registro de salud |
| `GET` | `/api/salud/` | Listar registros |
| `GET` | `/api/salud/{id}/` | Detalle de registro |
| `PATCH` | `/api/salud/{id}/` | Actualizar registro |
| `DELETE` | `/api/salud/{id}/` | Eliminar registro |

### Antropometría

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/antropometria/` | Crear medición |
| `GET` | `/api/antropometria/` | Listar mediciones |
| `GET` | `/api/antropometria/{id}/` | Detalle de medición |
| `PATCH` | `/api/antropometria/{id}/` | Actualizar medición |
| `DELETE` | `/api/antropometria/{id}/` | Eliminar medición |

### Rendimiento

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/rendimiento/` | Crear test de rendimiento |
| `GET` | `/api/rendimiento/` | Listar tests |
| `GET` | `/api/rendimiento/{id}/` | Detalle de test |
| `PATCH` | `/api/rendimiento/{id}/` | Actualizar test |
| `DELETE` | `/api/rendimiento/{id}/` | Eliminar test |

### Lesiones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/lesiones/` | Registrar lesión |
| `GET` | `/api/lesiones/` | Listar lesiones |
| `GET` | `/api/lesiones/{id}/` | Detalle de lesión |
| `PATCH` | `/api/lesiones/{id}/` | Actualizar lesión |
| `DELETE` | `/api/lesiones/{id}/` | Eliminar lesión |

### Rehabilitación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/rehabilitacion/` | Crear plan de rehabilitación |
| `GET` | `/api/rehabilitacion/` | Listar planes |
| `GET` | `/api/rehabilitacion/{id}/` | Detalle de plan |
| `PATCH` | `/api/rehabilitacion/{id}/` | Actualizar plan |
| `DELETE` | `/api/rehabilitacion/{id}/` | Eliminar plan |

### Dietas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/api/dietas/` | Crear plan de dieta |
| `GET` | `/api/dietas/` | Listar dietas |
| `GET` | `/api/dietas/{id}/` | Detalle de dieta |
| `PATCH` | `/api/dietas/{id}/` | Actualizar dieta |
| `DELETE` | `/api/dietas/{id}/` | Eliminar dieta |

---

## Stack tecnológico

- **Backend:** Python 3.12, Django 5, Django REST Framework
- **Base de datos:** PostgreSQL 16
- **Autenticación:** JWT (djangorestframework-simplejwt)
- **Servidor WSGI:** Gunicorn
- **Proxy inverso:** Nginx
- **Gestor de dependencias:** uv
- **CI/CD:** GitHub Actions
- **Infraestructura:** Azure VM (Ubuntu 22.04)

---

## CI/CD

El proyecto usa GitHub Actions para correr los tests automáticamente en cada push y desplegar en la VM cuando los tests pasan en la rama `main`.

Pipeline: `Tests → Deploy → Health check`
