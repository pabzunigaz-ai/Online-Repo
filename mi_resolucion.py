estudiantes = []
opcion_prev = 0

def main():
    print("---- Menu Principal ----")
    print("1. Añadir Estudiante")
    print("2. Buscar Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Actualizar Estado de Aprobación")
    print("5. Mostrar todos los Estudiantes")
    print("6. Salir")

def opción_validación():
    try:
        opción_validada = int(input("Elija una opcion 1-6: "))
        if opción_validada > 6:
            print("Elija una opción de 1-6.")
        else:
            return opción_validada
    except ValueError:
        print("Opción invalida")
        print("Solo se aceptan números")
        return

def añadir_estudiante(lista):
    nombre = input("Cual es el nombre del estudiante a añadir: ")
    matricula = input(f"Cual es el ID de {nombre}: ")
    nota_promedio = input("Cual fue la nota promedio del Estudiante: ")
    if not nombre_validación(nombre):
        print("EL nombre no puede estar vacio")
        return
    if not matricula_validación(matricula):
        print("Este campo tiene que ser entre 1.0 y 7.0")
    if not promedio_validación(nota_promedio):
        print("La nota promedio debe ser 0 o mayor.")
    
    estudiante = {
        'nombre': nombre,
        'matricula': int(matricula),
        'nota_promedio': float(nota_promedio),
        'estado_aprobación': False
    }
    lista.append(estudiante)
    print("El estudiante fue agregado al sistema.")
#Validaciónes
def nombre_validación(estudiante):
    return estudiante != ""

def matricula_validación(matricula_str):
    try:
        matricula_int = int(matricula_str)
        return matricula_int >= 0
    except ValueError:
        return False

def promedio_validación(nota_str):
    try:
        nota_float = int(nota_str)
        return 0.9 < nota_float < 7.1
    except ValueError:
        return False
#FIN

def buscar_estudiante(lista, estudiante):
    for i in range (len(lista)):
        if estudiante.strip().lower() == lista[i]['nombre'].strip().lower():
            return i
    return -1

def actualizar_aprobacion(lista):
    for i in lista:
        if i['nota_promedio'] >= 4.0:
            i['estado_aprobación'] = True

while opcion_prev != 6:
    main()
    opcion_prev = opción_validación()

    if opcion_prev == 1:
        añadir_estudiante(estudiantes)
    elif opcion_prev == 2:
        nombre_buscar = input("Ingrese un nombre a buscar: ")
        posicion = buscar_estudiante(estudiantes, nombre_buscar)

        if posicion != -1:
            estudiante_encontrado = estudiantes[posicion]
            print(f"Nombre: {estudiante_encontrado['nombre']}")
            print(f"ID: {estudiante_encontrado['matricula']}")
            print(f"Promedio: {estudiante_encontrado['nota_promedio']}")
        else:
            print(f"El estudiante {nombre_buscar} no fue encontrado.")
    elif opcion_prev == 3:
        try:
            ID_buscar = int(input("Ingrese un ID: "))
        except ValueError:
            print("El ID tiene que ser números.")

        for i in (estudiantes):
            if ID_buscar == i['matricula']:
                nombre  = i['nombre']
                posicion = buscar_estudiante(estudiantes, nombre)
        
        if posicion != -1:
            estudiantes.pop(posicion)
            print(f"Estudiante id {ID_buscar} fue eliminado.")
        else:
            print(f"El estudiante id {ID_buscar} no fue encontrado.")

    elif opcion_prev == 4:
        actualizar_aprobacion(estudiantes)
        print("El estado de aprobación fue actualizado.")
    elif opcion_prev == 5:
        actualizar_aprobacion(estudiantes)

        for i in estudiantes:
            print(f"Nombre: {i['nombre']}")
            print(f"ID: {i['matricula']}")
            print(f"Nota Promedio: {i['nota_promedio']}")
            if i['estado_aprobación']:
                print("Estado de aprobacion: Aprobado")
            else:
                print("Estado de aprobación: Desaprobado")
    elif opcion_prev == 6:
        print("Saliendo.")
        break