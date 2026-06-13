from django.db import models


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('Coach', 'Coach'),
        ('Usuario', 'Usuario'),
    ])

    class Meta:
        db_table = 'tipo_usuario'
        managed = False

    def __str__(self):
        return self.rol


class Medida(models.Model):
    id_medida = models.SmallAutoField(primary_key=True)
    nombre_med = models.CharField(max_length=50)

    class Meta:
        db_table = 'medidas'
        managed = False

    def __str__(self):
        return self.nombre_med


class Nivel(models.Model):
    id_nivel = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'niveles'
        managed = False

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=10, choices=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ])
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)
    edad = models.SmallIntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, unique=True)
    objetivo = models.CharField(max_length=100, null=True, blank=True)
    disciplina_preferida = models.CharField(max_length=100, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    id_tipo_usuario = models.ForeignKey(
        TipoUsuario, db_column='id_tipo_usuario', on_delete=models.PROTECT
    )
    id_medida = models.ForeignKey(
        Medida, db_column='id_medida', on_delete=models.SET_NULL, null=True, blank=True
    )
    nivel_usuario = models.SmallIntegerField(null=True, blank=True)

    foto_perfil = models.CharField(
    max_length=255,
    null=True,
    blank=True
    )

    class Meta:
        db_table = 'usuarios'
        managed = False

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_rol(self):
        return self.id_tipo_usuario.rol if self.id_tipo_usuario else None


class TipoEjercicio(models.Model):
    id_tipo = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'tipo_ejercicio'
        managed = False

    def __str__(self):
        return self.nombre


class Ejercicio(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_ejercicio = models.ForeignKey(
        TipoEjercicio, db_column='tipo_ejercicio', on_delete=models.SET_NULL, null=True
    )
    equipo_necesario = models.TextField(null=True, blank=True)
    nivel_dificultad = models.CharField(max_length=10, choices=[
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    ])
    instrucciones = models.TextField(null=True, blank=True)
    url_video = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'ejercicio'
        managed = False

    def __str__(self):
        return self.nombre


class VideoEjercicio(models.Model):
    id_video = models.AutoField(primary_key=True)

    ejercicio = models.ForeignKey(
        Ejercicio,
        db_column='id_ejercicio',  # 🔥 ESTA LÍNEA ES LA CLAVE
        on_delete=models.CASCADE,
        related_name='videos'
    )

    url = models.TextField()

    class Meta:
        db_table = 'video_ejercicio'
        managed = False  # 🔥 IMPORTANTE en tu caso

    def __str__(self):
        return f"Video de {self.ejercicio.nombre}"


class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    id_nivel = models.ForeignKey(
        Nivel, db_column='id_nivel', on_delete=models.SET_NULL, null=True
    )
    disciplina = models.CharField(max_length=100, null=True, blank=True)
    duracion_total = models.CharField(max_length=50, null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'rutina'
        managed = False

    def __str__(self):
        return self.nombre


class RutinaEjercicio(models.Model):
    id_rutina_ejercicio = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(
        Rutina, db_column='id_rutina', on_delete=models.CASCADE
    )
    id_ejercicio = models.ForeignKey(
        Ejercicio, db_column='id_ejercicio', on_delete=models.CASCADE
    )
    dia_semana = models.CharField(max_length=10, choices=[
        ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'), ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'), ('Domingo', 'Domingo'),
    ])
    orden = models.SmallIntegerField(null=True, blank=True)
    repeticiones = models.SmallIntegerField(null=True, blank=True)
    series = models.SmallIntegerField(null=True, blank=True)
    descanso = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'rutina_ejercicio'
        managed = False


class RutinaUsuario(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, db_column='id_usuario', on_delete=models.CASCADE
    )
    id_rutina = models.ForeignKey(
        Rutina, db_column='id_rutina', on_delete=models.CASCADE
    )
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=12, choices=[
        ('Activa', 'Activa'),
        ('Finalizada', 'Finalizada'),
        ('Pausada', 'Pausada'),
    ], default='Activa')
    adaptaciones_personalizadas = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'rutina_usuario'
        managed = False




class Seguimiento(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, db_column='id_usuario', on_delete=models.CASCADE
    )
    id_ejercicio = models.ForeignKey(
        Ejercicio, db_column='id_ejercicio', on_delete=models.CASCADE
    )
    fecha = models.DateField()
    repeticiones_realizadas = models.SmallIntegerField(null=True, blank=True)
    series_realizadas = models.SmallIntegerField(null=True, blank=True)
    peso_usado = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'seguimiento'
        managed = False


class Logro(models.Model):
    id_logro = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    requisito = models.TextField(null=True, blank=True)
    valoracion_num = models.SmallIntegerField(null=True, blank=True)
    estado = models.CharField(max_length=12, choices=[
        ('Disponible', 'Disponible'),
        ('Bloqueado', 'Bloqueado'),
        ('Alcanzado', 'Alcanzado'),
    ])
    cantidad = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'logros'
        managed = False

    def __str__(self):
        return self.nombre


class UsuarioLogro(models.Model):
    id_usuario = models.ForeignKey(
        Usuario, db_column='id_usuario', on_delete=models.CASCADE,
        primary_key=True
    )
    id_logro = models.ForeignKey(
        Logro, db_column='id_logro', on_delete=models.CASCADE
    )
    fecha_obtenida = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'usuario_logro'
        managed = False
        unique_together = (('id_usuario', 'id_logro'),)


class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, db_column='id_usuario', on_delete=models.CASCADE
    )
    mensaje = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=[
        ('Leída', 'Leída'),
        ('No Leída', 'No Leída'),
    ], default='No Leída')

    class Meta:
        db_table = 'notificacion'
        managed = False


class ValoracionProfesional(models.Model):
    id_valoracion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, db_column='id_usuario', on_delete=models.CASCADE
    )
    fecha_valoracion = models.DateField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    id_medida = models.ForeignKey(
        Medida, db_column='id_medida', on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = 'valoracion_profesional'
        managed = False


# ======================================================
# 🔥 NUEVOS MODELOS FLEXFIT (GESTIÓN DE ENTRENAMIENTO)
# ======================================================

class RutinaUsuarioDia(models.Model):
    id_rutina_usuario_dia = models.AutoField(primary_key=True)

    id_rutina_usuario = models.ForeignKey(
        RutinaUsuario,
        db_column='id_rutina_usuario',
        on_delete=models.CASCADE,
        related_name='dias'
    )

    dia_semana = models.CharField(max_length=10, choices=[
        ('Lunes','Lunes'), ('Martes','Martes'), ('Miércoles','Miércoles'),
        ('Jueves','Jueves'), ('Viernes','Viernes'),
        ('Sábado','Sábado'), ('Domingo','Domingo'),
    ])

    class Meta:
        db_table = 'rutina_usuario_dia'
        unique_together = ('id_rutina_usuario', 'dia_semana')

    def __str__(self):
        return f"{self.id_rutina_usuario} - {self.dia_semana}"


class SesionEntrenamiento(models.Model):
    id_sesion = models.AutoField(primary_key=True)

    id_rutina_usuario = models.ForeignKey(
        RutinaUsuario,
        on_delete=models.CASCADE
    )

    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    duracion_segundos = models.IntegerField(default=0)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"Sesion {self.id_sesion}"


class EjercicioSesion(models.Model):
    id = models.AutoField(primary_key=True)

    id_sesion = models.ForeignKey(
        SesionEntrenamiento,
        on_delete=models.CASCADE
    )

    id_rutina_ejercicio = models.ForeignKey(
        RutinaEjercicio,
        on_delete=models.CASCADE
    )

    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id_sesion} - {self.id_rutina_ejercicio}"
    

    