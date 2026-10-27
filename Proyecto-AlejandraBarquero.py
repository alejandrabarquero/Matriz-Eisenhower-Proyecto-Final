#Versión: 3
#Autora: Alejandra Barquero Núñez 
#Proyecto Final: Software de gestión de tareas con el
#sistema de la matriz Eisenhower

tareas = []
def menu_principal():
        #entrada: se le pide al usuario la opción con la que quiera empezar     #hacer el programa en general mejor con
                                                                                #sub menús en cada función para que no sea tan complicado 
                                                                                #que el usuario solo escriba el número de la opciónque ocupa 
        #proceso: se despliegan las opciones para el usuario 
        #según la opción que elija se ejecuta el código 
        #salida: se ejecuta la opción que el usuario escoja 
        while True:
                print("1. Agregar tareas")
                print("2. Consultar tareas")
                print("3. Modiifcar tareas")
                print("4. Eliminar tareas")
                print("5. Clasificación de tareas")
                print("6. Resumen de tareas")
                print("7. Salir")

                opcion = input("Elija una opción: ")

                if opcion == "1":
                        def agregarTarea ():
                            global tareas 
                            #entrada: se le pregunta al usuario por los datos de la/ las tareas 
                            #proceso: se guardan datos y se clasifica según categoría
                            #salida: las tareas son agregadas y guardadas 
                            nombre = input("Digite el nombre de la tarea: ")
                            descripcion = input("Describa su tarea: ") 
                            categoria = ""
                            print("Nivel de prioridad")
                            print("1. Urgente")
                            print("2. No urgente")
                            urgencia = (input("Elija una opción: "))

                            print("Nivel de importancia")
                            print("1.Importante")
                            print("2.No importante")
                            importancia = input("Elija una opción: ")
                            if urgencia == "1" and importancia == "1": 
                                        categoria = "Hacer"
                            elif urgencia == "2" and importancia == "1":
                                        categoria = "Decidir"
                            elif urgencia == "1" and importancia == "2":
                                        categoria = "Delegar"
                            elif urgencia == "2" and importancia == "2":
                                        categoria = "Eliminar"      
                            tarea = {"nombreTarea" :nombre.lower(), "descripcionTarea" : descripcion, "categoriaTarea" : categoria}
                            tareas.append(tarea)
                            print("Tarea guardada")
                        agregarTarea()
                elif opcion == "2":
                        def consultarTarea():
                            #entrada: con un ciclo for se entra en el diccioanrio       
                            for tarea in tareas:  
                                #proceso: con condicionales se dividen 
                                #las tareas en las categorías 
                                if tarea["categoriaTarea"] == "Hacer":
                                    print(F"""Importante y Urgente:""",tarea["nombreTarea"])
                                elif tarea["categoriaTarea"] == "Decidir":
                                    print(F"""Importante pero no urgente:""",tarea["nombreTarea"])
                                elif tarea["categoriaTarea"] == "Delegar":
                                    print(F"""Urgente pero no importante:""",tarea["nombreTarea"])
                                elif tarea["categoriaTarea"] == "Eliminar":
                                    print(F"""Ni urgente ni importante:""",tarea["nombreTarea"])
                                    #salida : aparecen las tareas con su 
                                    #respectiva categoría 
                        consultarTarea()
                elif opcion == "3":
                        def modificarTarea():
                            print("-----Tareas guardadas:----- ")
                            for tarea in tareas: 
                                  print("*", tarea["nombreTarea"])
                            print("----------------------------------")
                            #entrada: se le pide al susuario cuál tarea quiere actualizar 
                            #cambiar el nombre, descripción, prioridad e importacia de la 
                            #tarea
                            tareaActualizada = input("Digite el nombre de la tarea que desea actualizar: ")
                            for tarea in tareas: 
                                #proceso: con la información nueva proporcionada por el usuario 
                                #se crean variables nuevas con su respectivo valor y se 
                                #clasifica todo en base a la información que el usurio da 
                                if tareaActualizada.lower() == tarea["nombreTarea"].lower():
                                        nombreActualizado = input("Digite nuevo nombre de tarea: ")
                                        descripcionActualizado = input("Digite nueva descripción: ")
                                        print("Nivel de prioridad") #el print va antes del input para que se 
                                                        #vean las opciones 
                                        print("1. Urgente")
                                        print("2.No urgente")
                                        urgenciaActualizado = input("Digite nuevo nivel de prioridad: ")
                                        print("Nivel de importancia")
                                        print("1. Importante")
                                        print("2.No importante")
                                        importanciaActualizado = input("Digite nuevo nivel de importancia: ")
                                        tarea["nombreTarea"] = nombreActualizado.lower() # no poner + porque eso solo junta pero
                                                                                                        # no cambia el valor 
                                        tarea["descripcionTarea"] =  descripcionActualizado
                                        #ponemos un if dentro de un if y hay que identarlo 
                                        #para que funcione bien 
                                        if  urgenciaActualizado == "1" and importanciaActualizado == "1": 
                                            tarea["categoriaTarea"]  = "Hacer"
                                        elif urgenciaActualizado == "2" and importanciaActualizado == "1":
                                            tarea["categoriaTarea"] = "Decidir"
                                        elif urgenciaActualizado == "1" and importanciaActualizado == "2":
                                            tarea["categoriaTarea"]  = "Delegar"
                                        elif urgenciaActualizado == "2" and importanciaActualizado == "2":
                                            tarea["categoriaTarea"] = "Eliminar"
                                        print("Tarea modificada")
                                        #salida: se modifican las tareas y se clasifican 
                        modificarTarea()
                elif opcion == "4":
                        def eliminarTarea():
                            #entrada: se le pide al usuario escoger la tarea que 
                            #desea eliminar 
                            global tareas
                            print("-----Tareas guardadas:----- ")                         #ponerle una opción de 
                                                                                         # está seguro que quiere eliminar tarea
                                                                                         # para que haya un respaldo por si el usuario 
                                                                                         # se equivoca al eliminar alguna tarea 
                            for tarea in tareas: 
                                  print("*", tarea["nombreTarea"])
                            print("----------------------------------")
                            #proceso: con ciclo for se busca la tarea 
                            buscarNombre = input("Digite el nombre de la tarea que desea eliminar: ")
                            tareaEncontrada = None
                            for tarea in tareas: 
                                if buscarNombre.lower() == tarea["nombreTarea"].lower():
                                        tareaEncontrada = tarea
                                        break
                                        #tareas es la lista 
                                        #de ahí quitamos la tarea no de tarea el diccionario 
                            if tareaEncontrada != None: 
                                        tareas.remove(tareaEncontrada)      # no se usé el del porque el del
                                                                            # ocuparía todas las posiciones de la tarea 
                                                                            # con .remove() es más sencillo  
                                        print("Tarea eliminada")
                                        #salida: se elimina la tarea 
                            else: 
                                  print("No se encontró tarea")  
                        eliminarTarea()
                elif opcion == "5":
                        def clasificarTarea():
                            # entrada: se recopila la información 
                            print(F"""HACER:""")
                            for tarea in tareas:
                            #proceso: con condicionales se dividen 
                            #las tareas en las categorías 
                                if tarea["categoriaTarea"] == "Hacer":
                                    print(tarea["nombreTarea"])
                            print(F"""DECIDIR:""")
                            for tarea in tareas:
                                if tarea["categoriaTarea"] == "Decidir":
                                    print(tarea["nombreTarea"])
                            print(F"""DELEGAR:""")        
                            for tarea in tareas: 
                                if tarea["categoriaTarea"] == "Delegar":
                                    print(tarea["nombreTarea"])
                            print(F"""ELIMINAR:""")
                            for tarea in tareas:
                                if tarea["categoriaTarea"] == "Eliminar":
                                    print(tarea["nombreTarea"])
                                # salida: se muestran las tareas en la categoría 
                                # que correspnde 
                        clasificarTarea()
                elif opcion == "6":
                        # entrada: se obtiene información 
                        def resumenTarea():
                            print(F"""HACER:""")
                            contadorTarea = 0 # el contador cuenta las veces 
                                                # que algo sucede 
                            # proceso: usando el for y un contador se iría por categoria 
                            #contando la cantidad de tareas 
                            for tarea in tareas:
                                if tarea["categoriaTarea"] == "Hacer":
                                 contadorTarea = contadorTarea +1
                            print(contadorTarea)
                            
                            print(F"""DECIDIR:""")
                            contadorTarea = 0
                            for tarea in tareas:
                                if tarea["categoriaTarea"] == "Decidir":
                                    contadorTarea = contadorTarea +1
                            print(contadorTarea)
                            
                            print(F"""DELEGAR:""")    
                            contadorTarea = 0    
                            for tarea in tareas: 
                                if tarea["categoriaTarea"] == "Delegar":
                                    contadorTarea = contadorTarea +1
                            print(contadorTarea)
                            
                            print(F"""ELIMINAR:""")
                            contadorTarea = 0
                            for tarea in tareas:
                                if tarea["categoriaTarea"] == "Eliminar":
                                    contadorTarea = contadorTarea +1
                            print(contadorTarea)
                            # salida: se mostraría el total de las tareas por categoría 
                            # al usuario
                        resumenTarea()
                elif opcion == "7":
                    print("¡Adiós!")
                    break
menu_principal() 
