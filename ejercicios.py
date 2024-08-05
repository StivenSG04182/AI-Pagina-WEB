
""" lista=["Ana", "Luis", "Pedro", "Marta", "Sofía"]
if lista== "Luis":
    print("Juan esta en la lista")
else:
    print("Juan no esta en la lista")
    lista.append("Juan")

print(lista) """

# Crear un archivo que contenga los datos de los estudiantes de algoritmos (nombre, apellido, edad, nota parcial (entre 0 y 100), nota final (entre 0 y 100))
# una vez ingresado los datos, mostrar un menú con opciones: 1 mostrar estudiantes con promedio superior a 80, 2 cuantos estudiates pasaron los 2 examenes con un promedio mayor o igual a 60, 3 que muestre los nombres de los estudiantes con una edad menor a 22 años, 4 salir.


""" estudiantes = {}
promedios = {}
mayores_promedios = []
mayores_notas = []
menores_edad = []
pandequeso = True
while pandequeso:
        print ("************Bienvenido al sistema de estudiantes***********")
        print("estas son las opciones\n" "1.agregar estudiante.\n" "2.validar notas/datos.\n" "3.salir")
        pregunta = int (input ("que deseas realizar?: "))
        if pregunta == 1:
            nombre = input ("ingresa el nombre del estudiante: ")
            edad = int (input("ingresa la edad del estudiante: "))
            nota1 = int (input ("ingresa la nota del primer examen: "))
            nota2 = int (input ("ingresa la nota del primer examen: "))
            promedio_notas = nota1 + nota2 / 2
            promedios[nombre] = {'nota 1': nota1, 'nota 2': nota2, 'promedio': promedio_notas}
            estudiantes[nombre] = {'edad': edad, 'promedio': promedio_notas}
        elif pregunta == 2:
             print("******bienvenido a validacion*****\nestas son nuestas opciones:\n" "1.validar por promedio.\n" "2.validar por nota.\n" "3.validar por edad.\n")
             subpregunta = int (input ("que validacion vamos a realizar?: "))
             if subpregunta == 1:
                  for nombre,datos in promedios.items():
                       if datos['promedio'] >= 80:
                            mayores_promedios.append((nombre,datos['promedio']))
                            print(f"los mayores promedios son {mayores_promedios}")
             elif subpregunta == 2:
                    for nombre,datos in promedios.items():
                       if datos['nota 1'] >= 60 and datos['nota 2'] >= 60:
                            mayores_notas.append((nombre,datos['nota 1'],datos['nota 2']))
                            print(f"las mayores notas son {mayores_notas}")
             elif subpregunta == 3:
                  for nombre, dato in estudiantes.items():
                       if dato['edad'] < 22:
                            menores_edad.append((nombre,dato['edad']))
                            print(f"los menores de edad son: {menores_edad}")
        elif pregunta == 3:
            print("hasta luego")
            print(estudiantes)
            with open("estudiantes.txt", "w")as archivo:
                for estudiantes in estudiantes.items():
                    for clave, valor in estudiantes.items():
                        archivo.write(f"{clave} = {valor}")
                        archivo.close()
            pandequeso = False """


#crear un programa que gestione el estado de las habitaciones en una clinica y guarde los datos en un archivo.
#debe solicitar el numero del paciante de la ambitación, nombre y apellido. debe permitir actualizar el numero de una habitación existente.
#debe guardar el estado de las habitaciones en un archivo.
""" 
habitaciones={}
while True:
    opciones=int(input(f"Ingresa la opción que más se acomode a su necesidad\n\n1° Agregar Paciente.\n2° Modificar Paciente.\n3° Guardar y salir.\n\nRespuesta: "))
    if opciones==1:
        clave=input("Ingresa el número de la habitación: ")
        valor=input("Ingresa el nombre y apellido del paciente: ")
        habitaciones[clave]=valor
        print(f"se ha agregado correctamente la información")

    elif opciones==2:
        Buscar_paciente=input("\nIngresa el número de la habitación que deseas buscar: ")
        if Buscar_paciente not in habitaciones:
            print("El número de la habitación no se encuentra registrada en sistema")
        else:
            print(f"\nEl número de la habitación es '{Buscar_paciente}' tiene como propietario: {habitaciones[Buscar_paciente]}\n----------------------------------------------\n")
            valor_new=input("Ingresa el nombre del nuevo paciente: ")
            habitaciones[clave]=valor_new
            print(f"se ha cambiado correctamente la información")

    elif opciones==3:
        with open("habitaciones.txt", "w" ) as archivo:
            for clave, valor in habitaciones.items():
                archivo.write(f"{clave} = {valor}\n")
                archivo.close()
                print("|Gracias por utilizar este software|")
        break       
 """



#Crear un programa que gestione la información de los clientes de 2 bancos (banco -A y banco-B), debe guardar la información en 2 archivos.abs
#debe solicitar la información del nombre, el banco que perteneci y el nombre de la cuenta.
#debe permitir actualizar la información de un banco existente.

""" bancoA={}
bancoB={}
while True:
    opciones=input(f"Ingresa el nombre del Banco que cuentas\n\nA° Banco #A.\nB° Banco #B.\n3° Guardar y salir.\n\nRespuesta: ").title()
    if opciones=='A':
        opciones_bancoA=int(input(f"Ingresa la Opción que deseas realizar\n1° Agregar cuenta.\n2° modificar cuenta.\n3° Guardar y salir.\n\nRespuesta"))
        if opciones_bancoA==1:
            clave=input("Ingresa el número de cuenta: ")
            valor=input("Ingresa el nombre del propietario: ")
            bancoA[clave]=valor
            print(f"se ha agregado correctamente la información")

        elif opciones_bancoA==2:
            Buscar_cuenta=input("\nIngresa el número de cuenta que deseas buscar: ")
            if Buscar_cuenta not in bancoA:
                print("El número de cuenta no se encuentra registrada en el banco")
            else:
                print(f"\nEl número de cuenta '{Buscar_cuenta}' tiene como propietario: {bancoA[Buscar_cuenta]}\n----------------------------------------------\n")
                valor_new=input("Ingresa el nombre del nuevo propietario: ")
                bancoA[clave]=valor_new
                print(f"se ha cambiado correctamente la información")

        elif opciones_bancoA==3:
            with open("Información_Banco_A.txt", "w" ) as archivo:
                for clave, valor in bancoA.items():
                    archivo.write(f"{clave}= {valor}\n")
                    archivo.close()
                    print("|Gracias por utilizar este software|")
                    
                    
    elif opciones=='B':
        opciones_bancoB=int(input(f"Ingresa la Opción que deseas realizar\n1° Agregar cuenta.\n2° modificar cuenta.\n3° Guardar y salir.\n\nRespuesta"))
        if opciones_bancoB==1:
            clave=input("Ingresa el número de cuenta: ")
            valor=input("Ingresa el nombre del propietario: ")
            bancoB[clave]=valor
            print(f"se ha agregado correctamente la información")

        elif opciones_bancoB==2:
            Buscar_cuenta=input("\nIngresa el número de cuenta que deseas buscar: ")
            if Buscar_cuenta not in bancoB:
                print("El número de cuenta no se encuentra registrada en el banco")
            else:
                print(f"\nEl número de cuenta '{Buscar_cuenta}' tiene como propietario: {bancoB[Buscar_cuenta]}\n----------------------------------------------\n")
                valor_new=input("Ingresa el nombre del nuevo propietario: ")
                bancoB[clave]=valor_new
                print(f"se ha cambiado correctamente la información")

        elif opciones_bancoB==3:
            with open("Información_Banco_B.txt", "w" ) as archivo:
                for clave, valor in bancoB.items():
                    archivo.write(f"{clave}= {valor}\n")
                    archivo.close()
                    print("|Gracias por utilizar este software|")
                

    elif opciones=='3':
        with open("Información_Banco_A.txt", "w" ) as archivo:
            for clave, valor in bancoA.items():
                archivo.write(f"{clave}= {valor}\n")
                archivo.close()
        with open("Información_Banco_B.txt", "w" ) as archivo:
            for clave, valor in bancoB.items():
                archivo.write(f"{clave}= {valor}\n")
                archivo.close()
        break """




#Crear un programa que gestione un diccionario electronico que permita agregar palabras con sus definiciones, buscar definiciones de sus palabras y guardar los datos en un archivo de texto.
#debe permitir al usuario buscar la definicion de una palabra existente.
""" 
diccionario={}
while True:
    opciones=int(input(f"Ingresa la opción que deseas realizar\n\n1° Agregar palabra nueva al diccionario.\n2° Buscar el significado a una palabra guardada.\n3° Guardar y salir.\n\nRespuesta: "))
    if opciones==1:
        clave=input("Ingresa la palabra que deseas agregar: ")
        valor=input("Ingresa la definición de la palabra: ")
        diccionario[clave]=valor
        print(f"{diccionario}\n----------------------------------------------\nLa palabra se ha agregado correctamente")
    elif opciones==2:
        Buscar_palabra=input("\nIngresa la palabra que deseas buscar: ")
        if Buscar_palabra not in diccionario:
            print("La palabra no se encuentra en el diccionario")
        else:
            print(f"\nLa palabra '{Buscar_palabra}' tiene como definición: {diccionario[Buscar_palabra]}\n----------------------------------------------\n")
    elif opciones==3:
        with open("diccionario.txt", "w") as archivo:
            for clave, valor in diccionario.items():
                archivo.write(f"{clave}: {valor}")
                archivo.write("\n")
                archivo.close()
        print("|Gracias por utilizar este software|")
        break """


# grafo

""" class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
        
    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        
        return node
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        
        if node.value == value:
            return True
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
print(tree.search(4))  # True
print(tree.search(9))  # False
print("Inorder traversal:")
tree.inorder_traversal(tree.root) """

# Grafo-2 
""" import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_imagen, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
print(fashion_mnist)

class_imagen=['T-shirt/top','Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'] """
""" print(f"{train_imagen.shape}\n{len(train_labels)}\n{train_labels}\n{test_images}\n{len(test_labels)}")
 """
""" plt.figure()
plt.imshow(train_imagen[0])
plt.colorbar()
plt.grid(False)
plt.show() """

""" train_imagen = train_imagen /255.0
test_images = test_images /255.0 

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_imagen[i], cmap=plt.cm.binary)
    plt.xlabel(class_imagen[train_labels[i]])
plt.show()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_imagen, train_labels, epochs=10)

test_loss, test_acc =model.evaluate(test_images, test_labels, verbose=2)

print(f'\nTest Accuracy: ', test_acc)

predictions = model.predict(test_images)
predictions[0]
np.argmax(predictions[0])

test_labels[0]

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label=np.argmax(predictions_array)
    if predicted_label== true_label:
        color='blue'
    else:
        color='red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_imagen[predicted_label],
                                100*np.max(predictions_array),
                                class_imagen[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()


i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()


num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()

img = test_images[1]
print(img.shape)

img = (np.expand_dims(img,0))
print(img.shape)

predictions_single=model.predict(img)
print(predictions_single)

plot_value_array(1, predictions_single[0], test_labels)
_ = plt.xticks(range(10), class_imagen, rotation=45)

np.argmax(predictions_single[0])
 """



""" ventas = []

def guardar_datos():
    with open('ventas.txt', 'w') as file:
        for venta in ventas:
            file.write(f"{venta['ID']},{venta['Monto']}\n")

def cargar_datos():
    global ventas
    try:
        with open('ventas.txt', 'r') as file:
            ventas = [{"ID": line.split(",")[0], "Monto": float(line.split(",")[1])} for line in file]
    except FileNotFoundError:
        ventas = []

cargar_datos()

while True:
    print("\n1. Registrar nueva venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar una venta por ID")
    print("4. Calcular total de ventas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_venta = input("Ingrese el ID de la venta: ")
        monto = float(input("Ingrese el monto de la venta: "))
        ventas.append({"ID": id_venta, "Monto": monto})
        guardar_datos()
    elif opcion == "2":
        for venta in ventas:
            print(f"ID: {venta['ID']}, Monto: {venta['Monto']}")
    elif opcion == "3":
        id_venta = input("Ingrese el ID de la venta a buscar: ")
        for venta in ventas:
            if venta["ID"] == id_venta:
                print(f"ID: {venta['ID']}, Monto: {venta['Monto']}")
                break
        else:
            print("Venta no encontrada")
    elif opcion == "4":
        total = sum(venta["Monto"] for venta in ventas)
        print(f"El total de ventas es: {total}")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente de nuevo.") """



pasajeros = []

def guardar_datos():
    with open('pasajeros.txt', 'w') as file:
        for pasajero in pasajeros:
            file.write(f"{pasajero['Nombre']},{pasajero['Tiquete']},{pasajero['Vuelo']},{pasajero['Clase']},{pasajero['Ciudad']},{pasajero['Aerolínea']}\n")

def cargar_datos():
    global pasajeros
    try:
        with open('pasajeros.txt', 'r') as file:
            pasajeros = [{"Nombre": line.split(",")[0], "Tiquete": line.split(",")[1], "Vuelo": line.split(",")[2], "Clase": line.split(",")[3], "Ciudad": line.split(",")[4], "Aerolínea": line.split(",")[5].strip()} for line in file]
    except FileNotFoundError:
        pasajeros = []

cargar_datos()

while True:
    print("\n1. Registrar nuevo pasajero y su tiquete")
    print("2. Mostrar todos los pasajeros y sus tiquetes")
    print("3. Buscar un pasajero por su nombre")
    print("4. Eliminar un pasajero y su tiquete por su nombre")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del pasajero: ")
        num_tiquete = input("Ingrese el número de tiquete: ")
        num_vuelo = input("Ingrese el número del vuelo: ")
        clase = input("Ingrese la clase (económica, ejecutiva, primera clase): ")
        ciudad_destino = input("Ingrese la ciudad de destino: ")
        aerolinea = input("Ingrese el nombre de la aerolínea: ")
        pasajeros.append({"Nombre": nombre, "Tiquete": num_tiquete, "Vuelo": num_vuelo, "Clase": clase, "Ciudad": ciudad_destino, "Aerolínea": aerolinea})
        guardar_datos()
    elif opcion == "2":
        for pasajero in pasajeros:
            print(f"Nombre: {pasajero['Nombre']}, Tiquete: {pasajero['Tiquete']}, Vuelo: {pasajero['Vuelo']}, Clase: {pasajero['Clase']}, Ciudad: {pasajero['Ciudad']}, Aerolínea: {pasajero['Aerolínea']}")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del pasajero a buscar: ")
        for pasajero in pasajeros:
            if pasajero["Nombre"] == nombre:
                print(f"Nombre: {pasajero['Nombre']}, Tiquete: {pasajero['Tiquete']}, Vuelo: {pasajero['Vuelo']}, Clase: {pasajero['Clase']}, Ciudad: {pasajero['Ciudad']}, Aerolínea: {pasajero['Aerolínea']}")
                break
        else:
            print("Pasajero no encontrado")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del pasajero a eliminar: ")
        pasajeros = [pasajero for pasajero in pasajeros if pasajero["Nombre"] != nombre]
        guardar_datos()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente de nuevo.")







empleados = []

def guardar_datos():
    with open('empleados.txt', 'w') as file:
        for empleado in empleados:
            file.write(f"{empleado['Nombre']},{empleado['ID']},{empleado['Categoría']},{empleado['Tazas']},{empleado['Ingresos']}\n")

def cargar_datos():
    global empleados
    try:
        with open('empleados.txt', 'r') as file:
            empleados = [{"Nombre": line.split(",")[0], "ID": line.split(",")[1], "Categoría": line.split(",")[2], "Tazas": int(line.split(",")[3]), "Ingresos": float(line.split(",")[4])} for line in file]
    except FileNotFoundError:
        empleados = []

cargar_datos()

while True:
    print("\n1. Registrar nuevo empleado")
    print("2. Registrar las ventas de café de un empleado")
    print("3. Mostrar todos los empleados y sus ventas")
    print("4. Buscar un empleado por su nombre")
    print("5. Eliminar un empleado")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        id_empleado = input("Ingrese el número de identificación: ")
        categoria = input("Ingrese la categoría (barista, gerente, repartidor): ")
        empleados.append({"Nombre": nombre, "ID": id_empleado, "Categoría": categoria, "Tazas": 0, "Ingresos": 0.0})
        guardar_datos()
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        tazas = int(input("Ingrese el número de tazas vendidas: "))
        ingresos = float(input("Ingrese los ingresos generados: "))
        for empleado in empleados:
            if empleado["Nombre"] == nombre:
                empleado["Tazas"] += tazas
                empleado["Ingresos"] += ingresos
                guardar_datos()
                break
        else:
            print("Empleado no encontrado")
    elif opcion == "3":
        for empleado in empleados:
            print(f"Nombre: {empleado['Nombre']}, ID: {empleado['ID']}, Categoría: {empleado['Categoría']}, Tazas: {empleado['Tazas']}, Ingresos: {empleado['Ingresos']}")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del empleado a buscar: ")
        for empleado in empleados:
            if empleado["Nombre"] == nombre:
                print(f"Nombre: {empleado['Nombre']}, ID: {empleado['ID']}, Categoría: {empleado['Categoría']}, Tazas: {empleado['Tazas']}, Ingresos: {empleado['Ingresos']}")
                break
        else:
            print("Empleado no encontrado")
    elif opcion == "5":
        nombre = input("Ingrese el nombre del empleado a eliminar: ")
        empleados = [empleado for empleado in empleados if empleado["Nombre"] != nombre]
        guardar_datos()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente de nuevo.")

