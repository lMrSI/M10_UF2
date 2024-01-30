import json

class user:
    def __init__(self, nombre, apellido, correo, contraseña, numero, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.numero = numero
        self.edad = edad

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo

    def getContraseña(self):
        return self.contraseña
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
    
    def getNumero(self):
        return self.numero
    
    def setNumero(self, numero):
        self.numero = numero
    
    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad

    def saludo(self):
            print(f"La clase user tiene nombre {self.nombre}, apellido {self.apellido}, correo {self.correo}, contraseña {self.contraseña}, numero {self.numero}, y edad {self.edad}.")

    def to_dict(self):
        return {
            "nombre" : self.nombre,
            "apellido" : self.apellido,
            "correo" : self.correo,
            "contraseña" : self.contraseña,
            "numero" : self.numero,
            "edad" : self.edad
        }
    
usuario = user("Cristian", "Cruz", "cristian_cruz@gmail.com", "4adfa09pt", 643568907, 23)
usuario.saludo()

usuario_json = json.dumps(usuario.to_dict(), indent=2)
print(usuario_json)
  
