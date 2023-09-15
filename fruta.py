print("   Salpicones el Pipe  ")
print("- - - - - - - - - - - - -  ")
print("1. Digitar las frutas que desae en su salpicon ")
print("2. Fruta orden ")
print("3. Fruta mas barata ")
print("4. Costo total del salpicon ")
canastas = []
opcion = 0  
id = 0

while opcion != 5:
    opcion = int(input("Ingrese un numero del menu... "))

    if opcion == 1:
        op = int(input("ingrese el numero de frutas que desea -> "))

        for f in range(op):
            fruta = {}
            id += 1
            fruta["id"] = id
            fruta["seleccion"] = input("digite la fruta -> ")
            fruta["precio"] = float(input("valor de la fruta > "))
            fruta["cantidad"] = int(input("cantidad de frutas -> "))
            canastas.append(fruta)

    elif opcion == 2:
        canastas_ordenadas = sorted(canastas, key=lambda x: x["precio"], reverse=True)
        print("Frutas ordenadas de mayor a menor precio:")
        for fruta in canastas_ordenadas:
            print(f"Fruta: {fruta['seleccion']}, Precio: {fruta['precio']}")

    elif opcion == 3:
        canastas_ordenadas = sorted(canastas, key=lambda x: x["precio"], reverse=False)
        print("Fruta mas cara ")
        print(canastas_ordenadas[-1]) 
        print("Fruta mas barata ")
        print(canastas_ordenadas[0])  

    elif opcion == 4:
         print("Total a pagar ")
         total=0
        
         for fruta in canastas:
           costo=fruta['precio']*fruta['cantidad'] 
           total+=costo   
         print(total)
    
     
    elif opcion ==5:
        print("Saliendo del programa") 
           
    else:print("Opcion invalida")

