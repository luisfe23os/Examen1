print("    welcome a Music Day  ")
print(" - - - - - - - - - - - - - ")
print("1. Registrar grupo musical.")
print("2. Mostrar bandas que no se han presentado. ")
print("3. Cambiar Hora de presentacion. ")
print("4. Retirar grupo musical. ")
print("5. ver lista de bandas registradas. ")
print("6. Salir. ")
op=9
bandas=[]
id=0

while op != 6:
    grupo={}
    op = int(input("Digite una opcion -> "))
    if op == 1:
        id+=1
        print("registro de grupos ")
        grupo["id"]=id
        grupo["nombre"]=input("Digite nombre de banda -> ")
        grupo["genero"]=input("Digite genero musical ->")
        grupo["hora"]=input("Digite hora de presentacion -> ")
        grupo["pago"]=float(input("valor pagado -> "))
        print("Digite el numero que corresponda a la situacion de la banda... ")
        grupo["estado"]=input("1- si ya se presento O 2- si no se ha presentado -> ")
        print(f"Se ha completado el registro su ID para la presentacion es -> {grupo['id']}")
        bandas.append(grupo)
    elif op == 2:
        grupos_no_presentados = []  # Crear una lista para almacenar grupos no presentados
        for grupo in bandas:
            if grupo["estado"] == "2":#validacion 
                grupos_no_presentados.append(grupo)  # Agregar el grupo a la lista
        if grupos_no_presentados:
            print("Grupos que no se han presentado:")
            for grupo in grupos_no_presentados:
                print(f"{grupo['id']}, {grupo['nombre']}")
        else:
            print("Aun no hay grupos que no se hayan presentado ;)")
        

    elif op == 3:
        id_ba= int(input("ingrese el id del grupo que desea cambiar su hora de presentacion ->  "))

        for grupo in bandas:
            if grupo["id"] == id_ba :   
                if grupo["estado"]=="2":#validar si el grupo se ha presentado o no para poder realizar el cambio
                    nhora=input("Ingrese la nueva hora de presentacion -> ")
                    grupo["hora"]=nhora
                    print("se ha actualizado la hora de presentacion :) ")
                    print(f"{grupo['id']},{grupo['nombre']},{grupo['hora']}")
                    break
                else:
                    print("la banda ya se presento por lo cual no se puede cambiar la hora... ")
                break
        else:
            print("no se ha encontrado una banda con el id ingresado. ")
    elif op == 4:
            print("En esta opción vas a eliminar un grupo musical de la presentación")
            id_ba = int(input("Ingrese el ID de la banda que desea retirar: "))
            banda_eliminada = None 

            for grupo in bandas:
             if grupo["id"] == id_ba:
               banda_eliminada = grupo["nombre"]  #guardar la banda en la nueva variable
               bandas.remove(grupo) 
               break 
    
            if banda_eliminada is not None:# instrucion  para validar si se ha elimando el grupo 
             print(f"Se ha eliminado la banda con ID {id_ba} y nombre {banda_eliminada}")
            else:
             print("No se ha encontrado una banda con el ID indicado ;)")
    elif op==5:
        print("lista de bandas registradas. ")
        print(bandas)
    elif op ==6:
        print("saliendo del programa... ")   
        
    else:
        print("opcion invalida ;) ")


