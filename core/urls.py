from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),


    # ── ADMIN ──────────────────────────────────────────────
    path('admin-panel/usuarios/', views.admin_usuarios, name='admin_usuarios'),
    path('admin-panel/usuarios/crear/', views.admin_crear_usuario, name='admin_crear_usuario'),
    path('admin-panel/usuarios/<int:pk>/editar/', views.admin_editar_usuario, name='admin_editar_usuario'),
    path('admin-panel/usuarios/<int:pk>/eliminar/', views.admin_eliminar_usuario, name='admin_eliminar_usuario'),
    path('admin-panel/usuarios/<int:pk>/cambiar-rol/', views.admin_cambiar_rol, name='admin_cambiar_rol'),
    path('rutina/<int:rutina_id>/agregar-ejercicio/', views.agregar_ejercicio_rutina, name='agregar_ejercicio_rutina'),
    path('admin-panel/ejercicios/', views.admin_ejercicios, name='admin_ejercicios'),

    path('admin-panel/rutinas/', views.admin_rutinas, name='admin_rutinas'),
    path('admin-panel/rutinas/crear/', views.admin_crear_rutina, name='admin_crear_rutina'),
    path('admin-panel/rutinas/<int:pk>/editar/', views.admin_editar_rutina, name='admin_editar_rutina'),
    path('admin-panel/rutinas/<int:pk>/eliminar/', views.admin_eliminar_rutina, name='admin_eliminar_rutina'),

    path('admin-panel/tipos-ejercicio/', views.admin_tipos_ejercicio, name='admin_tipos_ejercicio'),
    path('admin-panel/tipos-ejercicio/crear/', views.admin_crear_tipo_ejercicio, name='admin_crear_tipo_ejercicio'),
    path('admin-panel/tipos-ejercicio/<int:pk>/editar/', views.admin_editar_tipo_ejercicio, name='admin_editar_tipo_ejercicio'),
    path('admin-panel/tipos-ejercicio/<int:pk>/eliminar/', views.admin_eliminar_tipo_ejercicio, name='admin_eliminar_tipo_ejercicio'),

    # ── COACH ──────────────────────────────────────────────
    path('coach/mis-usuarios/', views.coach_usuarios, name='coach_usuarios'),
    path('coach/rutinas/', views.coach_rutinas, name='coach_rutinas'),
    path('coach/rutinas/crear/', views.coach_crear_rutina, name='coach_crear_rutina'),
    path('coach/rutinas/<int:pk>/editar/', views.coach_editar_rutina, name='coach_editar_rutina'),
    path('coach/rutinas/<int:pk>/eliminar/', views.coach_eliminar_rutina, name='coach_eliminar_rutina'),
    path('coach/rutinas/<int:pk>/asignar/', views.coach_asignar_rutina, name='coach_asignar_rutina'),

    path('rutina/<int:rutina_id>/ver/', views.ver_rutina, name='ver_rutina'),
    path('coach/ejercicios/', views.coach_ejercicios, name='coach_ejercicios'),
    path('coach/ejercicios/crear/', views.coach_crear_ejercicio, name='coach_crear_ejercicio'),
    path('coach/ejercicios/<int:pk>/editar/', views.coach_editar_ejercicio, name='coach_editar_ejercicio'),
    path('coach/ejercicios/<int:pk>/eliminar/', views.coach_eliminar_ejercicio, name='coach_eliminar_ejercicio'),

    path('coach/tipos-ejercicio/', views.coach_tipos_ejercicio, name='coach_tipos_ejercicio'),
    path('coach/tipos-ejercicio/crear/', views.coach_crear_tipo_ejercicio, name='coach_crear_tipo_ejercicio'),
    path('coach/tipos-ejercicio/<int:pk>/editar/', views.coach_editar_tipo_ejercicio, name='coach_editar_tipo_ejercicio'),
    path('coach/tipos-ejercicio/<int:pk>/eliminar/', views.coach_eliminar_tipo_ejercicio, name='coach_eliminar_tipo_ejercicio'),


path(
    'coach/asignacion/<int:pk>/finalizar/',
    views.coach_finalizar_asignacion,
    name='coach_finalizar_asignacion'
),
    # ── USUARIO ────────────────────────────────────────────
    path('usuario/mi-rutina/', views.usuario_rutina, name='usuario_rutina'),
    path('usuario/progreso/', views.usuario_progreso, name='usuario_progreso'),
    path('usuario/progreso/agregar/', views.usuario_agregar_progreso, name='usuario_agregar_progreso'),
    path('usuario/logros/', views.usuario_logros, name='usuario_logros'),
    path('usuario/explorar-rutinas/', views.usuario_explorar_rutinas, name='usuario_explorar_rutinas'),
    path('usuario/rutinas/<int:pk>/seleccionar/', views.usuario_seleccionar_rutina, name='usuario_seleccionar_rutina'),

    # Notificaciones (todos los roles)
    path('notificaciones/', views.notificaciones_view, name='notificaciones'),
    path('notificaciones/<int:pk>/leer/', views.marcar_leida, name='marcar_leida'),
path(
    'notificaciones/marcar-todas/',
    views.marcar_todas_leidas,
    name='marcar_todas_leidas'
),


    # Perfil
    path('perfil/', views.perfil_view, name='perfil'),

    # ── ÍTEM 1: Carga masiva ──────────────────────────────────────────────────
    path('admin-panel/carga-masiva/', views.carga_masiva, name='carga_masiva'),

    # ── ÍTEM 2: YouTube ───────────────────────────────────────────────────────
    path('ejercicio/<int:pk>/videos/', views.youtube_ejercicio, name='youtube_ejercicio'),

    # ── ÍTEM 3: Reportes ─────────────────────────────────────────────────────
    path('admin-panel/reportes/', views.reportes, name='reportes'),

    path('usuario/iniciar-rutina/<int:pk>/', views.usuario_iniciar_rutina, name='usuario_iniciar_rutina'),
    path('usuario/ejecutar-rutina/<int:pk>/', views.usuario_ejecutar_rutina, name='usuario_ejecutar_rutina'),
    path('usuario/completar-ejercicio/<int:pk>/', views.completar_ejercicio),
    path('usuario/finalizar-rutina/<int:pk>/<int:tiempo>/', views.finalizar_rutina),
    path('reportes/exportar/', views.exportar_reportes_excel, name='exportar_reportes'),


    path(
    'rutina-ejercicio/<int:pk>/editar/',
    views.editar_rutina_ejercicio,
    name='editar_rutina_ejercicio'
),

path(
    'rutina-ejercicio/<int:pk>/eliminar/',
    views.eliminar_rutina_ejercicio,
    name='eliminar_rutina_ejercicio'
),


path(
    'rutina/<int:rutina_id>/planificacion/',
    views.editar_planificacion_rutina,
    name='editar_planificacion_rutina'
),


path(
    'rutina-ejercicio/<int:pk>/mover/',
    views.mover_ejercicio_dia,
    name='mover_ejercicio_dia'
),

path(
    'coach/asignacion/<int:pk>/editar/',
    views.editar_asignacion_rutina,
    name='editar_asignacion_rutina'
),



]
