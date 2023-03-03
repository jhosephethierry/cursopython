def calcularpagamento(quantidadehoras, valorhora):
   
    horas = float(quantidadehoras)
    taxa = float(valorhora)
    
    if horas <= 40:
       salario = horas * taxa
   
    else:
       horasexcedentes = horas - 40
       salario = 40 * taxa + (horasexcedentes * (1.5 * taxa))
    
    print(salario)
    
    return(salario)

calcularpagamento(120, 7)
    
        