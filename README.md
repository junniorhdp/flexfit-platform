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
- Seguimiento de progreso
- Sistema de logros
- Diseño responsive
- Integración de APIs

## Estado

Proyecto en desarrollo activo.

## Autor

Llunior Alirio Gonzalez Ochoa

---

# Guía de Instalación

## Requisitos previos

- Python 3.10+
- XAMPP (Apache + MySQL)
- Base de datos `flexfit`

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configurar la base de datos

Verifica los datos de conexión en:

```python
FLEXFIT/settings.py
```

## Cargar datos base

Importa o ejecuta:

```sql
datos_base.sql
```

## Ejecutar migraciones

```bash
python manage.py migrate --run-syncdb
```

## Crear administrador

```bash
python setup_admin.py
```

## Ejecutar servidor

```bash
python manage.py runserver
```

Abrir:

```
http://127.0.0.1:8000
```

## Estructura principal

```text
FLEXFIT/
├── core/
├── FLEXFIT/
├── manage.py
├── requirements.txt
├── datos_base.sql
└── setup_admin.py
```