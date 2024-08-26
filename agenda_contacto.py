

def mostarar_menu():
  print("\nAgenda de contactos:")
  print("1. Agregar contacto")
  print("2. Eliminar contacto")
  print("3. Buscar contacto")
  print("4. Listar contacto")
  print("5. Salir del programa")
  print("\n")
    
def agregar_contacto(agenda):
    nombre = input("Por favor introdusca el nombre completo del contacto: ")
    telefono = input("Por favor introdusca el telefono del contacto: ")
    email = input("Por favor introdusca el email del contacto: ")
    agenda[nombre] = {'telefono':telefono, 'email':email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")

    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")

    else: 
       print(f"No de ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que est buscando: ")

    if nombre in agenda:
       print(f"Nombre: {nombre}" )
       print(f"Telefono: {agenda[nombre]['telefono']}")
       print(f"Email: {agenda[nombre]['email']}")
    else:
       print(f"El contacto {nombre} no ha sido encontrado en la egenda")

def listar_contacto(agenda):
    if agenda: 
       print("\nLisat de contactos: ")
       for nombre,info in agenda.items():
          print(f"Nombre: {nombre}")
          print(f"Telefono: {info['telefono']}")
          print(f"Email: {info['email']}")
    else: 
       print("La agebda aun esta está vacia")
   

def agenda_contactos():
    agenda = {}

    while True :
       mostarar_menu()
       opcion = input("por favor elija una opcion: ")
       print("\n")
       if opcion == "1":
          agregar_contacto(agenda)
       elif opcion == "2":
          eliminar_contacto(agenda)
       elif opcion == "3":
          buscar_contacto(agenda)
       elif opcion == "4":
          listar_contacto(agenda)
       elif opcion == "5":
          print("Saliendo de la agenda de contactos !Hasta luego¡")
          break
       else:
          print("Por favor seleccione una opcon valida(del 1 al 5)")

agenda_contactos()