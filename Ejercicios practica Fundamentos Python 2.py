# %%
#A. LISTAS
#1. crear una lista de Notas
#Complete la lista con cinco notas
#y muestre la cantidad de elementos

notas = [3.0, 4.2, 4.5, 5.0]
print(len(notas))
print(notas)
# %%

#2. Acceder por índice 
# Use índices para imprimir la primera, 
# la tercera y la última temperatura.

temperaturas = [18, 20, 19, 21, 22]
print(temperaturas[1])
print(temperaturas[2])
print(temperaturas[3])

# %%

#3.Actualizar un elemento
# Corrija la segunda venta, que fue registrada como 80 pero
# debía ser 85.
ventas =[120, 80, 200, 50]
ventas [1] = 85
print (ventas)

# %%
# 4. Agregar y extraer datos
#Agregue una nueva nota y extraiga la última 
#nota registrada.
notas = [3.5, 4.0, 2.8]
notas.append (4.6)
ultima = notas.pop () 
print (ultima)
print (notas)

# %%
## 5. Calcular promedio
#Complete el acumulador para calcular 
# el promedio de una lista.
notas = [4.2, 3.8, 5.0, 2.9]
total = 0

for nota in notas:
    total = total + nota

promedio = total / len(notas)
print(round(promedio, 2))

# %%
## 6. Contar aprobados
##Cuente cuántas notas son mayores o iguales a 3.0.

notas = [4.2, 2.5, 3.0, 1.8, 4.7]
aprobados = 0

for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1

print(aprobados)

# %%
## 7. Filtrar valores válidos
## Construya una lista con las temperaturas que estén
## entre -10 y 50 grados.
 
lecturas = [18, 200, 21, -99, 19, 22]
validas = []

for t in lecturas:
    if t >= -10 and t <= 50:
        validas.append(t)
print(validas)    


# %%
## 8. Ordenar sin perder el original
## Use sorted() para crear una lista ordenada 
## sin modificar la lista inicial.

montos = [120000, 85000, 50000]
ordenados= sorted (montos)
print(montos)
print(ordenados)


# %%
## 9. Comprensión de listas
## Complete la comprensión para obtener los 
#  cuadrados de los números pares.

numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n*2 for n in numeros if n % 2==0]
print(cuadrados_pares)

# %%
## 10. Lista anidada
## Complete el doble ciclo para sumar todos 
## los elementos de una matriz.

matriz = [1, 2 , 3] , [4, 5, 6]
total = 0

for fila in matriz:
    for valor in fila:
        total += valor
print(total)

# %%
## B. Tuplas
##Datos fijos, desempaquetado y uso como clave
## 11. Crear una tupla fija
## Defina una tupla con la latitud y la longitud de una sede.

ubicacion = (7.50, -12.69)
print(ubicacion)
print(type(ubicacion))



# %%
## 12. Desempaquetar una tupla
## Asigne los elementos de la tupla a variables 
# con nombres significativos.

registro = ("A01", "LAURA", 4.6)
curso, nombre, nota = registro
print(nombre)
print(nota)

# %%
## 13. Tupla de un solo elemento
## Complete la sintaxis correcta de una tupla 
## que contiene un solo código.

codigo = ("A01", )
print(codigo)
print(type(codigo))

# %%
## 14. Convertir lista a tupla
## Convierta una lista de columnas a tupla para evitar 
## cambios accidentales.

columnas = ["fecha", "monto", "cliente"]

columnas_fijas = tuple(columnas)
print(columnas_fijas)

# %%

## 15. Retorno múltiple
## Complete una función que retorne el mínimo y el máximo 
# como una tupla implícita.

def resumen (valores):
    menor = min(valores)
    mayor = max(valores)
    return menor, mayor
minimo, maximo = resumen([8, 3, 10, 5])
print (minimo, maximo)

# %%
## 16. Reconocer inmutabilidad
## Ejecute mentalmente el código y explique qué error se produce.

punto = (10, 20)
punto [0] = 99
print (punto)
## Evita que datos constantes sean modificados durante una ejecucución.
 
# %%
## 17. Tupla como clave
## Use una tupla como clave para almacenar una lectura por coordenada.
lecturas = {}
coordenada = (4.65, -74.05)

lecturas [coordenada] = 18.5
print (lecturas[(4.65, -74.05)]) 

# %%
## 18. Combinar listas con zip
## Cree pares estudiante-nota usando zip() y conviértalos a lista.

nombres= ["Ana", "Luis", "Marta"]
notas=  [4.2, 3.8, 5.0]

pares = list(zip(nombres, notas))
print (pares)

# %%
## C. Diccionarios
# Pares clave-valor, acumuladores y registros 
## 19.  Crear un diccionario
## Complete las claves necesarias para representar a un estudiante.

estudiante = {
    "codigo": "A01",
    "nombre": "laura",
    "nota": 4.6
}
print (estudiante)

# %%
## 20. Acceso seguro con get()
## Use get() para consultar una clave que podría no existir.

cliente = {"nombre": "carlos", "puntaje": 720}
saldo = cliente.get("saldo",0)
print (saldo)

# %%
## 21. Actualizar valores
## Actualice el stock de un producto después de una venta de 3 unidades.

producto = {"codigo": "PO1", "stock": 8}
producto ["stock"] = producto ["stock"] - 3
print (producto["stock"])


# %%
## 22. Recorrer pares clave-valor
## Complete el recorrido para imprimir cada atributo con su valor.

producto = {"codigo": "P01", "precio": 12000, "stock": 8}
for clave, valor in producto.items():
    print (clave, valor)

# %%
## 23. Contar por categoría
## Use un diccionario acumulador para contar los tipos de transacción.

tipos = ["Debito", "Credito", "Debito", "Debito", "Credito"]
conteo = {}

for tipo in tipos:
    conteo[tipo] = conteo.get(tipo, 0)+ 1
print (conteo)


# %%
## 24. Diccionario anidado
## Acceda a la nota de Laura dentro de una estructura anidada.

grupo = {
    "A01":{"nombre": "laura", "nota": 4.6},
    "A02":{"nombre": "luis", "nota":3.8}
}
print (grupo["A01"]["nota"])

# %%
## 25. Lista de diccionarios
## Calcule el total de los montos en una lista de transacciones.

Transacciones = [
    {"Id":"T01", "monto":120000},
    {"Id":"T02", "monto":85000},
    {"Id":"T03", "monto":210000}
]
Total = 0

for T in Transacciones:
    Total += T ["monto"]
print (Total)

# %%
## 26. Buscar por código
## Complete una búsqueda lineal sobre una lista de diccionarios.

estudiantes = [
    {"codigo": "A01", "nombre": "Laura"},
    {"codigo": "A02", "nombre": "Luis"}
]
buscado = "A02"
resultado = None

for e in estudiantes:
    if e["codigo"] == "A02":
        resultado = e["nombre"]
print(resultado)

# %%
## 27. Filtrar diccionarios
## Construya una lista con los nombres de los estudiantes aprobados.

estudiantes = [
    {"nombre": "Ana", "nota": 4.2},
    {"nombre": "Luis", "nota": 2.8},
    {"nombre": "Marta", "nota": 3.5}
]
aprobados = []

for e in estudiantes:
    if e["nota"] >= 3.5:
        aprobados.append(e["nombre"])
print(aprobados)

# %%
## 28. Agrupar por estado
## Agrupe los nombres de los clientes según su nivel de riesgo.

clientes = [
    {"nombre": "Ana", "riesgo": "bajo"},
    {"nombre": "Luis", "riesgo": "alto"},
    {"nombre": "Marta", "riesgo": "bajo"}
]

grupo = {}

for c in clientes:
    riesgo = c["riesgo"]
    if riesgo not in grupo:
        grupo[riesgo] = []
    grupo[riesgo].append(c["nombre"])
print(grupo)

# %%
## 29. Inventario académico
## Complete el reporte de los productos con stock bajo.

inventario = [
    {"producto": "Marcador", "stock": 4},
    {"producto": "Cuaderno", "stock": 20},
    {"producto": "Borrador", "stock": 2}
]
bajos = []
for item in inventario:
    if item["stock"] < 5:
        bajos.append(item["producto"])
print(bajos)

# %%
## 30. Mini caso integrador
## Complete el algoritmo que calcula el total de los créditos 
# mayores o iguales a 100000 y registra los clientes correspondientes.

transacciones = [
    {"cliente": "Ana", "tipo": "Credito", "monto": 120000},
    {"cliente": "Luis", "tipo": "Debito", "monto": 85000},
    {"cliente": "Marta", "tipo": "Credito", "monto": 210000}
]

total_creditos = 0
clientes = []

for t in transacciones:
    if t["tipo"] == "Credito" and t["monto"] >= 100000:
        total_creditos += t["monto"]
        clientes.append(t["cliente"])
print(total_creditos)
print(clientes)
# %%
