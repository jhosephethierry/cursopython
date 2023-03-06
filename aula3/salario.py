def calcularpagamento(quantidadehoras, valorhora):
   
    horas = float(quantidadehoras)
    taxa = float(valorhora)
    
    if horas <= 40:
       salario = horas * taxa
   
    else:
       horasexcedentes = horas - 40
       salario = 40 * taxa + (horasexcedentes * (1.5 * taxa))
    
    return salario

horasstr = input("digite a quantidade de horas: ")
taxastr = input("digite o valor da taxa: ")

totalsalario = calcularpagamento(horasstr,taxastr)

print("o valor dos seus rendimentos é R$", totalsalario)    
        

    