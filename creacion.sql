-- DLL


-- Primero creamos la tabla de roles --
CREATE TABLE Roles (
    idRol INT AUTO_INCREMENT PRIMARY KEY,
    nombreRol VARCHAR(100) NOT NULL UNIQUE
);

-- Ahora creamos la tabla de usuarios relacionada a roles
CREATE TABLE Usuarios (
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    nombreUsuario VARCHAR(250) NOT NULL,
    correo VARCHAR(250) NOT NULL UNIQUE,
    fechaRegistro DATETIME NOT NULL, 
    -- Acá puede haber distinciones dependiendo comp planteamos el sistema. Quien creará el usuario? 
    -- Si el usuario lo crea un administrador, tal vez queramos que el administrador asigne el rol, 
    -- por lo que será necesario que tenga el NOT NULL
    -- Pero si el usuario se registra a si mismo, tal vez querramos asignarle un rol base por defecto 
    -- por lo que no seria necesario el NOT NULL, ya que automaticamente quedaría registrado con un rol
    -- "usuario"
    id_rol INT NOT NULL,

    -- FK == Foreign Key = Clave Foránea
    CONSTRAINT fk_rol FOREIGN KEY (id_rol) REFERENCES Roles(idRol)
);

-- DML 