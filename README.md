<<<<<<< HEAD
# FlexFit Platform

Plataforma web de entrenamiento personalizada desarrollada con Django.

## Tecnologías
- Python
- Django
- MySQL
- HTML5
- CSS3
- JavaScript

## Funcionalidades
- Sistema de autenticación
- Panel administrativo
- Gestión de rutinas y ejercicios
- Diseño responsive
- Integración de APIs

## Estado
Proyecto en desarrollo activo.

## Autor
Llunior Alirio Gonzalez Ochoa
=======
# FLEXFIT · Guía de Instalación

## Requisitos previos
- Python 3.10+ instalado
- XAMPP corriendo (Apache + MySQL)
- La base de datos `flexfit` ya creada con sus 14 tablas

---

## Paso 1 · Instalar dependencias

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install django mysqlclient
```

> Si tienes problemas con `mysqlclient` en Windows, descarga el wheel desde:
> https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

---

## Paso 2 · Configurar la base de datos

En `FLEXFIT/settings.py` ya está configurado para XAMPP por defecto:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flexfit',
        'USER': 'root',
        'PASSWORD': '',       # <-- Si tu MySQL tiene contraseña, agrégala aquí
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

---

## Paso 3 · Cargar datos base en phpMyAdmin

1. Abre phpMyAdmin → selecciona la BD `flexfit`
2. Ve a la pestaña **SQL**
3. Copia y pega el contenido de `datos_base.sql` y ejecuta

Esto inserta los tipos de usuario, niveles, medidas y tipos de ejercicio.

---

## Paso 4 · Crear las sesiones de Django

```bash
python manage.py migrate --run-syncdb
```

> Como los modelos usan `managed = False`, Django solo creará la tabla de sesiones.

---

## Paso 5 · Crear el usuario Admin

```bash
python setup_admin.py
```

Esto crea el usuario con credenciales:
- **Usuario:** `admin`
- **Contraseña:** `Admin1234`

---

## Paso 6 · Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000**

---

## Rutas principales

| Ruta | Descripción |
|------|-------------|
| `/` | Login |
| `/registro/` | Registro público (Usuario/Coach) |
| `/dashboard/` | Panel según rol |
| `/admin-panel/usuarios/` | CRUD usuarios (Admin) |
| `/admin-panel/ejercicios/` | CRUD ejercicios (Admin) |
| `/admin-panel/rutinas/` | CRUD rutinas (Admin) |
| `/coach/rutinas/` | Gestión rutinas (Coach) |
| `/coach/ejercicios/` | Gestión ejercicios (Coach) |
| `/usuario/mi-rutina/` | Ver rutinas activas (Usuario) |
| `/usuario/progreso/` | Registrar sesiones (Usuario) |
| `/usuario/logros/` | Ver logros (Usuario) |

---

## Estructura del proyecto

```
FLEXFIT/
├── FLEXFIT/
│   ├── settings.py       ← Configuración y BD
│   └── urls.py           ← URLs raíz
├── core/
│   ├── models.py         ← Modelos (mapped a BD existente)
│   ├── views.py          ← Toda la lógica
│   ├── urls.py           ← URLs de la app
│   ├── templates/core/
│   │   ├── base.html     ← Layout con sidebar
│   │   ├── login.html    ← Login + Registro
│   │   ├── dashboard.html
│   │   ├── admin/        ← Vistas Admin
│   │   ├── coach/        ← Vistas Coach
│   │   └── usuario/      ← Vistas Usuario
│   └── static/core/css/
│       └── main.css      ← Estilos negro/azul
├── manage.py
├── setup_admin.py        ← Crea el admin inicial
├── datos_base.sql        ← SQL con datos base
└── requirements.txt
```
>>>>>>> e09dc6b (Initial commit - FlexFit platform)
