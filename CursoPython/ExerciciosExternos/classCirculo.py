class Circulo:

    def __init__(self,raio):
        
        self.raio = raio
        self.diametro = raio * 2
   
    def Area (self):
       
        Area = 3.14 *  (self.raio * 2)
        return Area
    
    def Circuferencia (self):
        
        Circuferencia = self.diametro * self.raio
        return Circuferencia

circulo1 = Circulo(5)

print(circulo1.Area())
print(circulo1.Circuferencia())
    