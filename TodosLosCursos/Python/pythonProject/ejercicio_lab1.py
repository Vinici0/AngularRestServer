from abc import ABC, abstractmethod


class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color.lower()
        
    def __str__(self):
        return f"Color: {self.color}"


class FiguraGeomatrica(ABC):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho
        
    #No se puede instanciar un metodo abstracto
    @abstractmethod
    def calcular_area(self):
        pass
        
    def __str__(self):
        return f"Alto: {self.alto} - Ancho: {self.ancho}"
    

class Rectangulo(FiguraGeomatrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeomatrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f"{Color.__str__(self)} - {FiguraGeomatrica.__str__(self)} -Area: {self.area()}"
    
class Cuadrado(FiguraGeomatrica, Color):
    def __init__(self, lado, color):
        FiguraGeomatrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f"{Color.__str__(self)} - {FiguraGeomatrica.__str__(self)} - Area: {self.area()}"
    
    
if __name__ == "__main__":
    rectangulo = Rectangulo(10, 20, "Rojo")
    print(rectangulo)
    
    cuadrado = Cuadrado(10, "Verde")
    print(cuadrado)