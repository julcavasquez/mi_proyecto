# Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, 
# editorial y autor(es). Considerar que un libro puede tener varios autores.
import csv
import json


class Libro:
    __id = ''
    titulo = ''
    genero = ''
    __isbn = ''
    editorial = ''
    autores = ''

# **** Constructor de la clase ****
    # def __init__(self,id,titulo,genero,isbn,editorial,autores):
    #     self.__id = id
    #     self.titulo = titulo
    #     self.genero = genero
    #     self.__isbn = isbn
    #     self.editorial = editorial
    #     self.autores = autores
# **** Fin Constructor de la clase ****

# **** Creando getters y setters ****
    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id
    
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self,isbn):
        self.__isbn = isbn
# **** Fin getters y setters ****



# **** Menú de opciones ****

def mostrar_menu(opciones):
    print('Menú de opciones:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Seleccionar Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    print(opcion_salida)
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1: Leer archivo de disco duro.', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Opción 3', accion4),
        '5': ('Opción 3', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


global lista 
lista = list()
def accion1():       
    print('Has elegido la opción 1')   
    with open("libros.csv", "r") as File:
        lista.clear()
        reader = csv.DictReader(File)
        for row in reader:
            lista.append(row)

def accion2():
    print('Has elegido la opción 2')
    #print(lista)
    for l in lista:
        print(l)



def accion3():
    print('Agregando un libro')
    libro = Libro()
    lista_autores = []
    libro.set_id(len(lista) + 1)
    libro.titulo = input("Ingrese titulo libro: ")
    libro.genero = input("Ingrese genero libro: ")
    isbn = input("Ingrese isbn libro: ")
    libro.set_isbn(isbn)
    libro.editorial = input("Ingrese editorial libro: ")
    autores = input("Ingrese autor del libro: ")
    lista_autores.append(autores)
    continuar = input("Desea ingresar otro autor (S/N): ")
    while continuar != 'N':
        autores = input("Ingrese autor del libro: ")        
        continuar = input("Desea ingresar otro autor (S/N): ")
        lista_autores.append(autores)
    print(lista_autores)
    libro.autores = '/'.join(lista_autores)
    print("Gracias por su colaboración")
    lista.append(libro.__dict__)

def csv_borrar_datos():
    file = open("libros.csv", "w")
    file.close()

def accion4():
    csv_borrar_datos()
    with open('libros.csv', 'w',newline="") as csvfile:
        fieldnames = ['_Libro__id','titulo','genero','_Libro__isbn','editorial','autores']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for l in lista:
            writer.writerow(l)
    print("Writing complete")

def accion5():
    isbn_eliminar = input("Ingrese isbn de libro a eliminar: ")
    print(len(lista))
    index = -1
    for i in range(0,len(lista)):
        print(i)
        for clave, valor in lista[i].items():
            if (clave == '_Libro__isbn') and (valor == isbn_eliminar):
                print("eliminado")
                print(valor)
                print(clave)
                index = i
                break 
    lista.pop(index)               
    print(lista)

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()

# **** Fin Menú de opciones ****





  
