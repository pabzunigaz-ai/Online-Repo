lista_estudiantes = []
validated_option = 0

def main(): #Menu en texto
    print("="*3, "Main Menu", "="*3)
    print("1. Añade un Estudiante")
    print("2. Busca un Estudiante")
    print("3. Elimina un Estudiante")
    print("4. Actualizar Estado de aprovación")
    print("5. Mostrar Estudiantes")
    print("6. Salir")

def option_validation(): #Funcion para validar la opción ingresada
             try:
                 option_str = int(input("Ingrese una opción: "))
                 return option_str
             except ValueError:
                 print("Solo se aceptan números")

def agregar_estudiante(lista): #funcion para agregar estudiantes
             nombre = input("Ingrese el nombre del estudiante: ")
             if not estudiante_validation(nombre):
                   print("Este campo no puede estar vacio.")
                   return 
             
             matricula = input("Ingrese el ID del Estudiante: ")
             if not matricula_validation(matricula):
                print("EL número de ID tiene que ser igual o mayor a 0.")
                return
             id_verificado = int(matricula)
             for i in lista:
                   if i['matricula'] == id_verificado:
                         print("2 Estudiantes no pueden tener el mismo ID.")
                         return

             nota_promedio = input("Ingrese la nota promedio del Estudiante: ")
             if not promedio_validation(nota_promedio):
                   print("La nota debe ser entre 1.0 y 7.0.")
                   return
             
             alumno = {
                   'nombre': nombre,
                   'matricula': int(matricula),
                   'nota_promedio': float(nota_promedio),
                   'aprobado': False
             }
             
             lista.append(alumno)
             print("EL almuno a sido agregado al sistema.")

#Inicio: validaciónes
def promedio_validation(promedio):
            try:
                  promedio_int = float(promedio)
                  return 0.9 < promedio_int <= 7.0 
            except ValueError:
                  return False

def matricula_validation(numero):
            try:
                   numero_int = int(numero)
                   return numero_int >= 0 
            except ValueError:
                return False
                
def estudiante_validation(nombre_str):
             return nombre_str != ""
#Fin: Valicadiones

def buscar_estudiante(lista, nombre): #Funcion para buscar
            for i in range (len(lista)):
                if nombre.strip().lower() == lista[i]['nombre']:
                    return i
            return -1

def actualizar_estudiantes(lista):
      for i in lista:
            if i['nota_promedio'] >= 4.0:
                  i['nota_promedio'] = True

while validated_option != 6: #Menu, solo las opciones
    main()
    validated_option = option_validation()

    if validated_option == 1:
        agregar_estudiante(lista_estudiantes)
    elif validated_option == 2:
        nombre = input("Ingrese el nombre de un estudiante a buscar: ")
        posicion = buscar_estudiante(lista_estudiantes, nombre)

        if posicion != -1:
            estudiante = lista_estudiantes[posicion]
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Matricula: {estudiante['matricula']}")
            print(f"Nota promedio: {estudiante['nota_promedio']}")
        else:
            print(f"El estudiante '{nombre}' no se encuentra en nuestro sistema.")
    elif validated_option == 3:
        nombre = input("Ingrese un nombre a eliminar")
        posicion = buscar_estudiante(lista_estudiantes, nombre)

        if posicion != -1:
              estudiante = lista_estudiantes[posicion]
              print(f"El estudiante '{estudiante['nombre']}' eliminado")
              lista_estudiantes.pop(posicion)
        else:
              print(f"EL estudiante '{nombre}' no se encuentra en nuestro sistema.")
    elif validated_option == 4:
        actualizar_estudiantes(lista_estudiantes)
        print("El estado de aprobación se actualizo")
    elif validated_option == 5:
        actualizar_estudiantes(lista_estudiantes)
        if lista_estudiantes:
            for i in lista_estudiantes:
                print("\n")
                print(f"Estudiante: {i['nombre']}", "-"*20)
                print(f"ID: {i['matricula']}")
                print(f"Nota promedio: {i['nota_promedio']}")
                if i['aprobado']:
                    print("¡Aprobado!")
                else:
                    print("Lamentablemente, el estudiante desaprobo.")
                print("\n")
        else:
              print("No se encuentra registrado ningun estudiante")
    elif validated_option == 6:
        print("Hasta Luego!")
        break
    else:
        print()
