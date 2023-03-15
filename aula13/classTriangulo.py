class Triangulo:

    def __init__(self,LadoA,LadoB,LadoC):

        self.ladoa = LadoA
        self.ladob = LadoB
        self.ladoc = LadoC

    def calcularPerimetro(self,LadoA,LadoB,LadoC):
        
        self.perimetro = LadoA + LadoB + LadoC

    def getMaiorLado(self):
        pass


triagunlo1 = Triangulo(LadoA = int(input('Digite o lado A. ')), LadoB = int(input('Digite o lado B. ')), LadoC = int(input('Digite o lado C. ')))
