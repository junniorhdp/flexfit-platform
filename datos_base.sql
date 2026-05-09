-- ============================================================
-- FLEXFIT · Datos base para la BD MySQL
-- Ejecuta este script en phpMyAdmin sobre la BD "flexfit"
-- ============================================================

-- Tipos de usuario
INSERT IGNORE INTO tipo_usuario (id_tipo_usuario, rol) VALUES
(1, 'Admin'),
(2, 'Coach'),
(3, 'Usuario');

-- Niveles
INSERT IGNORE INTO niveles (id_nivel, nombre) VALUES
(1, 'Principiante'),
(2, 'Intermedio'),
(3, 'Avanzado');

-- Medidas
INSERT IGNORE INTO medidas (id_medida, nombre_med) VALUES
(1, 'kg'),
(2, 'lb'),
(3, 'cm'),
(4, 'BMI');

-- Tipos de ejercicio de ejemplo
INSERT IGNORE INTO tipo_ejercicio (id_tipo, nombre) VALUES
(1, 'Cardio'),
(2, 'Fuerza'),
(3, 'Flexibilidad'),
(4, 'HIIT'),
(5, 'Funcional');

-- Usuario Admin inicial
-- Contraseña: Admin1234
-- (hash generado con Django's make_password)
INSERT IGNORE INTO usuarios
  (nombre, apellido, genero, usuario, contrasena, edad, email, objetivo,
   disciplina_preferida, fecha_registro, id_tipo_usuario, nivel_usuario)
VALUES
  ('Administrador', 'FlexFit', 'Otro', 'admin',
   'pbkdf2_sha256$720000$defaultsalt$hashedpassword',
   NULL, 'admin@flexfit.com', 'Gestionar el sistema',
   'General', CURDATE(), 1, 1);

-- NOTA: El hash de arriba es un placeholder.
-- Usa el script setup_admin.py incluido para crear el admin con contraseña real.
