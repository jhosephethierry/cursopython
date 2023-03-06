def contaletras(palavra,letra): # define a função
    
    contador = 0 # cria uma variável contador iniciando em zero
    
    for l in palavra: # condição para
        
        if l.lower() == letra.lower(): # .lower() transforma a letra em minúscula pra haver distinção
            
            contador += 1 # incrementa o contador
            
    return contador # retorna o contador

pal = input("digite a(s) palavra(s): ")
let = input("digite uma letra da(s) palavra(s) digitada(s): ")

contagem = contaletras(pal,let)

print(f"a(s) letra(s) {let} aparece(m) {contagem} vez(es) na(s) palavra(s) {pal}")
