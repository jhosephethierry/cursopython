class Triangulo:

    def __init__(self,LadoA,LadoB,LadoC):

        self.ladoa = LadoA
        self.ladob = LadoB
        self.ladoc = LadoC

    def calcularPerimetro(self):
        
        perimetro = self.ladoa + self.ladob +self.ladoc
        return perimetro
    

triagunlo1 = Triangulo(LadoA = int(input('Digite o lado A. ')), LadoB = int(input('Digite o lado B. ')), LadoC = int(input('Digite o lado C. ')))

print(f'O perímetro do triangulo é {triagunlo1.calcularPerimetro()}.')