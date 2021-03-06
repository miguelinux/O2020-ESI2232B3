import csv
import os

archivo = ""
lector = ""

def abrir():
    global archivo
    global lector
    archivo = open("productos.csv","r")
    lector = csv.reader(archivo)


def imprimir_productos():
    print("Producto   Cantidad   Precio")
    print("---------------------------------")
    # Me salto una linea que es la cabecera del archivo CSV
    next(lector)
    for fila in lector:
        print(fila[0] + "   " + str(fila[2]) + "    " + str(fila[1]))
    print("")
    # Hay que regresar al principio
    archivo.seek(0)


def comprar():
    # Nos saltamos la primera linea
    next(lector)
    contador=1
    num_producto=0
    lista=[]
    for fila in lector:
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")
    archivo.seek(0)
    producto = str(input("¿Cual producto quieres comparar?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            print("")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        print("")
        return

    cantidad = int(input("Cantidad de producto: "))

    if cantidad < 1:
        print("La cantidad es invalida.")
        print("")
        return

    archivo_temporal = open("temporal.csv","w")
    escritor=csv.writer(archivo_temporal)
    for fila in lector:
        # Si el producto es el que estoy buscando
        if fila[0] == producto:
            # Verifico si tengo suficiente producto
            if cantidad > int(fila[2]):
                print("No hay suficiente producto")
            else:
                # Resto de mi stock la cantidad
                fila[2] = str(int(fila[2]) - cantidad)
            escritor.writerow(fila)
        else:
            escritor.writerow(fila)
    archivo_temporal.close()
    archivo.close()
    os.remove("productos.csv")
    os.rename("temporal.csv","productos.csv")
    abrir()


def surtir():
    # Nos saltamos la primera linea
    next(lector)
    contador=1
    num_producto=0
    lista=[]
    for fila in lector:
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")
    archivo.seek(0)
    producto = str(input("¿Cual producto quieres surtir?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            print("")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        print("")
        return

    cantidad = int(input("Cantidad de producto a surtir: "))

    if cantidad < 1:
        print("La cantidad es invalida.")
        print("")
        return

    archivo_temporal = open("temporal.csv","w")
    escritor=csv.writer(archivo_temporal)
    for fila in lector:
        # Si el producto es el que estoy buscando
        if fila[0] == producto:
            # Sumo la cantidad al producto actual
            fila[2] = str(int(fila[2]) + cantidad)
            escritor.writerow(fila)
        else:
            escritor.writerow(fila)
    archivo_temporal.close()
    archivo.close()
    os.remove("productos.csv")
    os.rename("temporal.csv","productos.csv")
    abrir()

def quitar():
    # Nos saltamos la primera linea
    next(lector)
    contador=1
    num_producto=0
    lista=[]
    for fila in lector:
        print(str(contador) + ".- " + fila[0])
        lista.append(fila[0])
        contador = contador+1
    print("")
    archivo.seek(0)
    producto = str(input("¿Cual producto quieres quitar?: "))
    # Verifico si es número o texto
    if producto.isnumeric():
        num_producto=int(producto)
        if num_producto < 1 or num_producto > contador-1:
            print("El producto no existe.")
            print("")
            return
        else:
            producto = lista[num_producto-1]

    if producto not in lista:
        print("El producto no existe")
        print("")
        return

    archivo_temporal = open("temporal.csv","w")
    escritor=csv.writer(archivo_temporal)
    for fila in lector:
        # Si el producto es diferente lo escribo en temporal
        if fila[0] != producto:
            escritor.writerow(fila)

    archivo_temporal.close()
    archivo.close()
    os.remove("productos.csv")
    os.rename("temporal.csv","productos.csv")
    abrir()


def agregar():
    global archivo
    nuevo_producto = ["nombre","precio","cantidad"]
    # Pedir al usuario el producto
    nuevo_producto[0] = str(input("Escribe el nombre del producto: "))
    # Pedir al usuario la cantidad
    nuevo_producto[2] = str(input("Escribe la cantidad del producto: "))
    # Pedir al usuario el precio
    nuevo_producto[1] = str(input("Escribe el precio del producto: "))
    # Abrir archivo para agregar al Final
    archivo.close()
    archivo = open("productos.csv","a")
    # Escribir en el archivo los datos recolectados
    escritor=csv.writer(archivo)
    escritor.writerow(nuevo_producto)
    archivo.close()
    abrir()



def menu():
    print("Menu de Productos")
    print("")
    print("1. Imprimir productos")
    print("2. Comparar algun producto")
    print("3. Surtir producto")
    print("4. Agregar producto")
    print("5. Quitar  producto")
    print("")
    print("6. Salir")
    print("")
    opcion = int(input("Opción: "))
    return opcion


def principal():
    opcion = 0
    # Abrir el archivo a usar
    abrir()
    # mientras opción es diferente de 4
    while opcion != 6:

        opcion = menu()

        if opcion == 1:
            imprimir_productos()
        elif opcion == 2:
                comprar()
        elif opcion == 3:
            surtir()
        elif opcion == 4:
            agregar()
        elif opcion == 5:
            quitar()
        elif opcion < 1 or opcion > 6:
            print("Opción Invalida")
            print("")



if __name__ == "__main__":
    principal()
