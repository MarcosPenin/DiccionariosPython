"""Ejercicio 1 Escribe un programa que lea una cadena y devuelva un diccionario 
con la cantidad de apariciones de cada carácter en la cadena.""" 

cadena=input("Introduce el texto para contar sus caracteres:").lower()

dict1={}

for char in cadena:
    if char not in dict1.keys():
        dict1[char]=1
    else:
        dict1[char]+=1

print(dict1)
    
        


