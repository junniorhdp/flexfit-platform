"""
importacion.py — Carga masiva de datos para FLEXFIT
Soporta archivos Excel (.xlsx) y CSV (.csv)
Modelos: Ejercicio, Usuario, Rutina
"""

import csv
import io
import openpyxl
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .models import Ejercicio, TipoEjercicio, Usuario, TipoUsuario, Rutina, Nivel


def _limpiar_cabecera(texto):
    """Elimina emojis, asteriscos y espacios extra del encabezado."""
    if not texto:
        return ''
    texto = str(texto).strip()
    limpio = ''
    for ch in texto:
        if ch.isalnum() or ch == '_' or ch == ' ':
            limpio += ch
    return limpio.strip().lower().replace(' ', '_')


def _leer_filas_excel(archivo):
    """Lee un archivo Excel ignorando filas vacías y filas de notas."""
    wb = openpyxl.load_workbook(archivo, read_only=True, data_only=True)
    ws = wb.active
    filas = list(ws.iter_rows(values_only=True))
    if not filas:
        return []

    # Limpiar cabeceras (quita ⚠, *, espacios raros)
    cabeceras = [_limpiar_cabecera(c) for c in filas[0]]

    resultado = []
    for fila in filas[1:]:
        # Ignorar filas completamente vacías
        if all(v is None for v in fila):
            continue
        # Ignorar filas de notas al pie
        primera = str(fila[0]).strip() if fila[0] is not None else ''
        if primera.startswith('⚠') or primera.startswith('•') or primera.upper().startswith('NOTA'):
            continue
        resultado.append({
            cabeceras[i]: (str(fila[i]).strip() if fila[i] is not None else '')
            for i in range(len(cabeceras))
        })
    return resultado


def _leer_filas_csv(archivo):
    """Lee un archivo CSV y devuelve lista de dicts."""
    contenido = archivo.read()
    try:
        texto = contenido.decode('utf-8-sig')
    except UnicodeDecodeError:
        texto = contenido.decode('latin-1')
    reader = csv.DictReader(io.StringIO(texto))
    return [{_limpiar_cabecera(k): v.strip() for k, v in row.items()} for row in reader]


def leer_archivo(archivo):
    nombre = archivo.name.lower()
    if nombre.endswith('.xlsx') or nombre.endswith('.xls'):
        return _leer_filas_excel(archivo)
    elif nombre.endswith('.csv'):
        return _leer_filas_csv(archivo)
    else:
        raise ValueError('Formato no soportado. Use .xlsx o .csv')


# ─── IMPORTAR EJERCICIOS ───────────────────────────────────────────────────────

def importar_ejercicios(archivo):
    filas = leer_archivo(archivo)
    creados = 0
    errores = []

    for i, fila in enumerate(filas, start=2):
        nombre = fila.get('nombre', '').strip()
        if not nombre:
            errores.append(f"Fila {i}: 'nombre' es obligatorio.")
            continue

        nivel = fila.get('nivel_dificultad', 'Bajo').strip().capitalize()
        if nivel not in ['Bajo', 'Medio', 'Alto']:
            nivel = 'Bajo'

        tipo_nombre = fila.get('tipo_ejercicio', '').strip()
        tipo_obj = None
        if tipo_nombre:
            tipo_obj, _ = TipoEjercicio.objects.get_or_create(nombre=tipo_nombre)

        try:
            ej, creado = Ejercicio.objects.get_or_create(
                nombre=nombre,
                defaults={
                    'tipo_ejercicio': tipo_obj,
                    'nivel_dificultad': nivel,
                    'equipo_necesario': fila.get('equipo_necesario', ''),
                    'instrucciones': fila.get('instrucciones', ''),
                    'url_video': fila.get('url_video', ''),
                }
            )
            if creado:
                creados += 1
            else:
                errores.append(f"Fila {i}: El ejercicio '{nombre}' ya existe (omitido).")
        except Exception as e:
            errores.append(f"Fila {i}: Error al guardar '{nombre}': {e}")

    return creados, errores


# ─── IMPORTAR USUARIOS ─────────────────────────────────────────────────────────

def importar_usuarios(archivo):
    filas = leer_archivo(archivo)
    creados = 0
    errores = []

    for i, fila in enumerate(filas, start=2):
        nombre = fila.get('nombre', '').strip()
        apellido = fila.get('apellido', '').strip()
        usuario_str = fila.get('usuario', '').strip()
        email = fila.get('email', '').strip()
        contrasena = fila.get('contrasena', '').strip()

        if not all([nombre, apellido, usuario_str, email, contrasena]):
            errores.append(f"Fila {i}: Faltan campos obligatorios (nombre, apellido, usuario, email, contrasena).")
            continue

        if Usuario.objects.filter(usuario=usuario_str).exists():
            errores.append(f"Fila {i}: El usuario '{usuario_str}' ya existe (omitido).")
            continue
        if Usuario.objects.filter(email=email).exists():
            errores.append(f"Fila {i}: El email '{email}' ya está registrado (omitido).")
            continue

        rol = fila.get('rol', 'Usuario').strip().capitalize()
        if rol not in ['Admin', 'Coach', 'Usuario']:
            rol = 'Usuario'

        try:
            tipo = TipoUsuario.objects.get(rol=rol)
            genero = fila.get('genero', 'Otro').strip().capitalize()
            if genero not in ['Masculino', 'Femenino', 'Otro']:
                genero = 'Otro'

            edad_str = fila.get('edad', '').strip()
            edad = int(edad_str) if edad_str.isdigit() else None

            Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                usuario=usuario_str,
                email=email,
                contrasena=make_password(contrasena),
                genero=genero,
                edad=edad,
                objetivo=fila.get('objetivo', ''),
                id_tipo_usuario=tipo,
                fecha_registro=timezone.now().date(),
            )
            creados += 1
        except TipoUsuario.DoesNotExist:
            errores.append(f"Fila {i}: Rol '{rol}' no encontrado en la base de datos.")
        except Exception as e:
            errores.append(f"Fila {i}: Error al crear usuario '{usuario_str}': {e}")

    return creados, errores


# ─── IMPORTAR RUTINAS ──────────────────────────────────────────────────────────

def importar_rutinas(archivo):
    filas = leer_archivo(archivo)
    creados = 0
    errores = []

    for i, fila in enumerate(filas, start=2):
        nombre = fila.get('nombre', '').strip()
        if not nombre:
            errores.append(f"Fila {i}: 'nombre' es obligatorio.")
            continue

        nivel_nombre = fila.get('nivel', '').strip()
        nivel_obj = None
        if nivel_nombre:
            nivel_obj = Nivel.objects.filter(nombre__iexact=nivel_nombre).first()

        try:
            r, creado = Rutina.objects.get_or_create(
                nombre=nombre,
                defaults={
                    'descripcion': fila.get('descripcion', ''),
                    'id_nivel': nivel_obj,
                    'disciplina': fila.get('disciplina', ''),
                    'duracion_total': fila.get('duracion_total', ''),
                    'comentario': fila.get('comentario', ''),
                }
            )
            if creado:
                creados += 1
            else:
                errores.append(f"Fila {i}: La rutina '{nombre}' ya existe (omitida).")
        except Exception as e:
            errores.append(f"Fila {i}: Error al guardar rutina '{nombre}': {e}")

    return creados, errores
