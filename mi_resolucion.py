list = []
option = 0

def main():
    print("="*3, "Main Menu", "="*3)
    print("1. Añade un Estudiante")
    print("2. Busca un Estudiante")
    print("3. Elimina un Estudiante")
    print("4. Actualizar Estado de aprovación")
    print("5. Mostrar Estudiantes")
    print("6. Salir")

def option_validation():
             try:
                 option_str = int(input("Ingrese una opción: "))
                 return option_str
             except ValueError:
                 print("Solo se aceptan números")

def agregar_estudiante(lista):
             nombre = input("Ingrese el nombre del estudiante: ")
             if not estudiante_validation(nombre):
                   print("Este campo no puede estar vacio.")
                   return
             
             matricula = input("Ingrese el ID del Estudiante: ")
             matricula_validated = matricula_validation(matricula)
             if not matricula_validated:
                print("EL número de ID tiene que ser igual o mayor a 0.")
                return

             nota_promedio = input("Ingrese la nota promedio del Estudiante: ")
             promedio_validated = promedio_validation(nota_promedio)
             if not promedio_validated:
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

def promedio_validation(promedio):
            try:
                  promedio_int = float(promedio)
                  return 0.9 < promedio_int <= 7.0 
            except ValueError:
                  return

def matricula_validation(id):
            try:
                   id_int = int(id)
                   return id_int >= 0 
            except ValueError:
                return
                
def estudiante_validation(nombre_str):
             return nombre_str != ""

def buscar_estudiante(lista, nombre):
            for i in range (len(lista)):
                if nombre.strip().lower() == lista[i]['nombre']:
                    return i
            return -1

while option != 6:
    main()
    validated_option = option_validation()

    if validated_option == 1:
        agregar_estudiante(list)
    elif validated_option == 2:
        nombre = input("Ingrese el nombre de un estudiante a buscar: ")
        posicion = buscar_estudiante(list, nombre)

        if posicion != -1:
            estudiante = list[posicion]
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Matricula: {estudiante['matricula']}")
            print(f"Nota promedio: {estudiante['nota_promedio']}")
        else:
            print(f"El estudiante '{nombre}' no se encuentra en nuestro sistema.")
    elif validated_option == 3:
        nombre = input("Ingrese un nombre a eliminar")
    elif validated_option == 4:
        print()
    elif validated_option == 5:
        print()
    elif validated_option == 6:
        print("Hasta Luego!")
        break
    else:
        print()
