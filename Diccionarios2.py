"""Vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará 
el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta """

dict1={"manzana":0.2,"pera":0.4, "piña":3.4, "fresa":0.15, "sandía":2.7}
flag=True
flag2=True
total=0

while flag:
    fruta=input("Introduce la fruta que has vendido:").lower()

    while flag2:
        try:
            num=int(input("¿Cuántas has vendido? "))
            flag2=False
        except ValueError:
            print("No has introducido un número válido")     

    try:
        print("La venta tendrá un importe de", dict1[fruta]*num),"euros"
        total+=dict1[fruta]*num
    except KeyError:
        print("Lo siento, esa fruta no se encuentra registrada.")   
    except:
        print("Error desconocido")
    finally: 
        continuar=input("Pulse s si desea realizar otra consulta:").lower()
        if continuar!="s":
            flag=False
        
print("El importe total será de",total,"euros" )       





