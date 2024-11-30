print(" ")#espacio
print("nolasco_aguilar_martha_sofia_0948_3W")#datos


class Agenda:#crea una clase
    def __init__(self):#define funcion
        self.contactos = []#lista vacia para contactos

    def anadir_contacto(self):#define funcion
        self.contactos.append(input("Nombre, Teléfono, Email: "))#solicita al usuario ingresar dichos datos

    def listar_contactos(self):#define funcion
        print("\n".join(self.contactos))#imprime resultado

    def buscar_contacto(self):#define funcion
        nombre = input("Nombre: ")#solicita ingresar nombre
        for contacto in self.contactos:#bucle for
            if contacto.startswith(nombre):#verifica si la condicion es verdadera
                print(contacto)#imprime valor de contacto
                return
        print("No encontrado.")#imprime mensaje

    def editar_contacto(self):#define funcion
        nombre = input("Nombre: ")#solicita ingresar nombre
        for i, contacto in enumerate(self.contactos):#bucle for
            if contacto.startswith(nombre):#verifica si la condicion es verdadera
                self.contactos[i] = input("Nuevo Nombre, Teléfono, Email: ")#solicita ingresar datos

    def menu(self):#define funcion
        opciones = {#abre opciones
            "1": self.anadir_contacto,#valor
            "2": self.listar_contactos,#valor
            "3": self.buscar_contacto,#valor
            "4": self.editar_contacto,#valor
            "5": exit#valor
        }#cierra opciones

        while True:#bucle while
            opcion = input("\n1. Añadir\n2. Lista\n3. Buscar\n4. Editar\n5. Salir\nOpción: ")#solicita una opcion a elegir
            if opcion in opciones:#verifica si la condicion es verdadera
                opciones[opcion]()#imprime opcion

agenda = Agenda()#clase agenda
agenda.menu()#muestra menu

