DicionarioA = {
    
    1: 10,
    2: 20,
    3: 30,
   
    }

DicionarioB = {
    
    4: 40,
    5: 50,
    6: 60,
   
    }

DicionarioC = {
    
    7: 70,
    8: 80,
    9: 90,
   
    }

DicionarioCocatenado = {**DicionarioA, **DicionarioB, **DicionarioC} # ** Asterisco duplo une dicionarios

print(DicionarioCocatenado)