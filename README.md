REGISTRO DE USUARIOS

El sistema permite editar o eliminar los contactos creados, tambien sera de forma obligatoria llenar los campos que se 
le asigne.
Incluye datos como: nombre, telefono y correo electronico
Herramientas Usadas:
- python
- SQLserver

![Image_Alt](https://github.com/Manu-Crack/SQLserverRegistro/blob/071ef7d75aad0d27fdb88eebafb6b2413ce92d74/image.png)

Creacion de la Base de datos,
comandos usados:

- CREATE DATABASE flaskContacto;
- GO
- USE flaskContacto;
- CREATE TABLE Usuario (
  - ID INT PRIMARY KEY IDENTITY(1,1),
  - nombre NVARCHAR(100) NOT NULL,
  - telefono NVARCHAR(20) NULL,
  - correo NVARCHAR(150) NULL
- );

![Image_Alt]()
