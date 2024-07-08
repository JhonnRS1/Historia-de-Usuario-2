class Cliente:
    def __init__(self, nombre, apellidos, correo, contraseña, dni, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.contraseña = contraseña
        self.dni = dni
        self.edad = edad

    def actualizar_perfil(self, nombre=None, apellidos=None, correo=None, contraseña=None, dni=None, edad=None):
        if nombre:
            self.nombre = nombre
        if apellidos:
            self.apellidos = apellidos
        if correo:
            self.correo = correo
        if contraseña:
            self.contraseña = contraseña
        if dni:
            self.dni = dni
        if edad:
            self.edad = edad

        return True
