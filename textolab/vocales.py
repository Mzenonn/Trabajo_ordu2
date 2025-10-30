def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for i in texto:
        if i in vocales:
            contador += 1
            
    
    return contador 

print(contar_vocales("Hola orduna")) 
