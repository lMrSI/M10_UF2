import json

class vehicle:
    def __init__(self, marca, modelo, año, color, precio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio = precio
        self.kilometraje = kilometraje

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getAño(self):
        return self.año
    
    def setAño(self, año):
        self.año = año

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio

    def getKilometraje(self):
        return self.kilometraje
    
    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def saludo(self):
            print(f"Este es un vehículo de marca {self.marca}, modelo {self.modelo}, año {self.año}, color {self.color}, precio {self.precio}, y con {self.kilometraje} kilómetros.")

    def to_dict(self):
            return {
                "marca": self.marca,
                "modelo": self.modelo,
                "año": self.año,
                "color": self.color,
                "precio": self.precio,
                "kilometraje": self.kilometraje
            }

car = vehicle("Toyota", "Camry", 2022, "Rojo", 25000, 12000)
car.saludo()

car_json = json.dumps(car.to_dict(), indent=2)
print(car_json)
  