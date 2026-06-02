# FLEXFIT · Plataforma Web de Gestión Fitness

FLEXFIT es una plataforma web desarrollada con Django orientada a la gestión de rutinas, ejercicios, progreso físico y administración de usuarios dentro de un entorno fitness.

El sistema implementa múltiples roles de usuario, control de rutinas, seguimiento de progreso y herramientas administrativas para gimnasios, entrenadores y usuarios finales.

---

# Características Principales

## Panel Administrativo

* Gestión completa de usuarios
* CRUD de ejercicios
* CRUD de rutinas
* Gestión de tipos de ejercicio
* Reportes del sistema
* Carga masiva de datos

## Panel Coach

* Creación y gestión de rutinas
* Gestión de ejercicios
* Asignación de rutinas a usuarios
* Administración de tipos de ejercicio

## Panel Usuario

* Visualización de rutinas activas
* Registro de progreso físico
* Ejecución de rutinas
* Sistema de logros
* Exploración de rutinas
* Seguimiento de sesiones

---

# Tecnologías Utilizadas

| Tecnología   | Uso                  |
| ------------ | -------------------- |
| Python 3     | Backend              |
| Django       | Framework web        |
| MySQL        | Base de datos        |
| HTML5        | Estructura frontend  |
| CSS3         | Estilos              |
| JavaScript   | Interactividad       |
| XAMPP        | Entorno local        |
| Git & GitHub | Control de versiones |

---

# Arquitectura del Proyecto

```text
FLEXFIT/
├── FLEXFIT/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│   ├── templates/
│   ├── static/
│   ├── templatetags/
│   └── management/
│
├── manage.py
├── setup_admin.py
├── datos_base.sql
├── requirements.txt
└── README.md
```

---

# Requisitos Previos

Antes de ejecutar el proyecto necesitas:

* Python 3.10 o superior
* XAMPP (Apache + MySQL)
* Git instalado
* Base de datos MySQL llamada `flexfit`

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/junniorhdp/flexfit-platform.git
```

```bash
cd flexfit-platform
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si `mysqlclient` genera errores en Windows:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

---

# Configuración de Base de Datos

En `FLEXFIT/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flexfit_',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Si tu instalación de MySQL tiene contraseña, reemplaza el valor de `PASSWORD`.

---

# Importar Datos Base

1. Abrir phpMyAdmin
2. Seleccionar la base de datos `flexfit`
3. Ir a la pestaña SQL
4. Ejecutar el contenido de:

```text
datos_base.sql
```

Esto cargará:

* tipos de usuario
* niveles
* medidas
* tipos de ejercicio
* datos iniciales del sistema

---

# Migraciones

```bash
python manage.py migrate --run-syncdb
```

> Nota: El proyecto utiliza modelos con `managed = False`, por lo que Django únicamente gestionará las tablas necesarias como sesiones y autenticación.

---

# Crear Usuario Administrador

```bash
python setup_admin.py
```

Credenciales por defecto:

| Usuario | Contraseña |
| ------- | ---------- |
| admin   | Admin1234  |

---

# Ejecutar el Proyecto

```bash
python manage.py runserver
```

Accede desde:

```text
http://127.0.0.1:8000
```

---

# Rutas Principales

| Ruta                       | Descripción             |
| -------------------------- | ----------------------- |
| `/`                        | Login                   |
| `/registro/`               | Registro público        |
| `/dashboard/`              | Dashboard principal     |
| `/admin-panel/usuarios/`   | Gestión de usuarios     |
| `/admin-panel/ejercicios/` | Gestión de ejercicios   |
| `/admin-panel/rutinas/`    | Gestión de rutinas      |
| `/coach/rutinas/`          | Rutinas del coach       |
| `/coach/ejercicios/`       | Ejercicios del coach    |
| `/usuario/mi-rutina/`      | Rutina activa           |
| `/usuario/progreso/`       | Seguimiento de progreso |
| `/usuario/logros/`         | Sistema de logros       |

---

# Seguridad y Configuración

Antes de desplegar el proyecto en producción:

* Cambiar `SECRET_KEY`
* Desactivar `DEBUG=True`
* Configurar variables de entorno
* Proteger credenciales de MySQL
* Configurar `ALLOWED_HOSTS`

---

# Control de Versiones

El proyecto utiliza Git y GitHub para el control de versiones.

Flujo básico de trabajo:

```bash
git add .
git commit -m "Descripción del cambio"
git push origin main
```

---

# Estado del Proyecto

Proyecto académico y funcional desarrollado como plataforma de gestión fitness utilizando Django y MySQL.

Actualmente incluye:

* autenticación por roles
* gestión de rutinas
* seguimiento de progreso
* sistema administrativo
* arquitectura modular escalable

---

# Autor

Desarrollado por:

**Junnior HDP**

Tecnólogo en Desarrollo de Software y Gestión Logística (SENA)

Especializado en:

* desarrollo backend con Python
* automatización de procesos
* Django
* MySQL
* integración de sistemas
* soluciones digitales
