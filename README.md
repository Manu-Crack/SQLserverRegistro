REGISTRO DE USUARIOS

El sistema permite editar o eliminar los contactos creados, tambien sera de forma obligatoria llenar los campos que se 
le asigne.
Incluye datos como: nombre, telefono y correo electronico
Herramientas Usadas:
- python
- SQLserver

![Image_Alt](https://github.com/Manu-Crack/SQLserverRegistro/blob/071ef7d75aad0d27fdb88eebafb6b2413ce92d74/image.png)

Creacion de la Base de datos:
comandos usados:
  CREATE DATABASE flaskContacto;
  GO
  USE flaskContacto;
  CREATE TABLE Usuario (
    ID INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(30),
    correo VARCHAR(255) UNIQUE
  );

![Image_Alt](https://github.com/Manu-Crack/SQLserverRegistro/blob/2d0bcf9acfa5faef3d2e2ce8737978eb3a05209f/image.png)
