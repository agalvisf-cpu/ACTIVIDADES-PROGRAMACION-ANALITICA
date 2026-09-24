# %%
import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"
data = pd.read_csv(url)
data = data.rename(columns={
 'Tax 5%': 'Tax',
 'Cost of goods sold': 'Cogs',
 'Gross margin percentage': 'Gross margin pct',
 'Customer stratification rating': 'Rating'
})
data.columns = (
 data.columns
 .str.strip()
 .str.lower()
 .str.replace(' ', '_')
)

# %%
# A. Conocer el DataFrame
# 1. Dimensiones del DataFrame
# Complete la instrucción para conocer el número de filas y de columnas
print(data.shape)
#1000 filas y 17 variables

# %%
# 2. Columnas, tipos y primeras filas
# Muestre los nombres de las columnas, el tipo de dato de cada una y las tres primeras
# ventas registradas.
print (data.columns) 
print (data.dtypes)
data.head (3)

# %%
# %%
# B. Seleccionar datos
# 3.Seleccionar varias columnas
# Construya un subconjunto que contenga únicamente product_line, quantity y total
resultado = data [['product_line', 'quantity', 'total']]
resultado. head()

# %%
# 4.¿Series o DataFrame?
# Antes de ejecutar, anote qué objeto devuelve cada línea. Después compruébelo
# Rta: 1 codigo devuelve una serie 2 Codigo devuelve un Dataframe
print (type(data["total"]))
print (type(data[["total"]])) 

# %%
# 5.  loc y iloc sobre la misma celda
# Las dos instrucciones deben mostrar la línea de producto de la fila con índice 7. La
# primera trabaja con etiquetas y la segunda con posiciones.
print(data.loc[7, "product_line"])
print(data.iloc[7, 5])
#Respuesta breve: Porque tendriamos que saber cual seria la posicion
#de la Columna que necesitamos. Es mas favorable llamarla por el nombre

# %%
# C. Filtrar filas
# Máscaras booleanas y condiciones combinadas
# 6. Una sola condición
#Conserve únicamente las ventas de más de ocho unidades y cuente cuántas son.
mascara = data["quantity"] > 8
resultado = data [mascara]
print ( resultado.shape[0])

# %%
#7. Dos condiciones al tiempo
#Obtenga únicamente las ventas de la sucursal 
#C cuyo total sea mayor de 300 USD.
mascara = (data["branch"] == "C") & (data["total"])> 300
resultado = data[mascara]
print (resultado.shape)

# %%
# PRUEBA
print(data[data['branch'] == 'C'].shape)
print(data[data['total'] > 300].shape)
print(data[(data['branch'] == 'C') & (data['total'] > 300)].shape)

# %%
# Codigo de Chatgpt
mascara = (data['branch'] == 'C') & (data['total'] > 300)
resultado = data[mascara]
print(resultado.shape)

# %%
# 8. Corregir un filtro por categorías
# La instrucción comentada falla porque or 
# no funciona entre columnas de pandas.
# Reescriba el filtro con una sola llamada 
# que reciba la lista de líneas de producto.

mascara = (data['product_line'] == 'Food and beverages') | (data['product_line'] == 'Fashion accessories')
data[mascara].shape

# %%
# 9. Rango de valores y columnas elegidas
# Obtenga las ventas de las sucursales A y C cuyo total se encuentre entre 200 y 500
# USD, mostrando solamente branch, product_line, quantity y total.

mascara = (data['branch'].isin(['A', 'C'])) & (data['total'].between(200, 500))
resultado = data.loc[mascara, ['branch', 'product_line', 'quantity', 'total']]
resultado.head()
#Respuesta: Permite obtener las filas y columnas en una sola instruccion haciendo
#el codigo mas corto sin pasos intermedios

# %%
# D. Crear información nueva
# Columnas derivadas sin ciclos
# 10. Valor de cada unidad vendida 
# Cree la columna valor_unitario dividiendo el total entre la cantidad. Resuélvalo sin
# escribir un ciclo for.
data ['valor_unitario'] = data ['total'] / data['quantity']
print (data['valor_unitario'].head(3).round(2))

# %%
# 11. Clasificar cada venta INTERMEDIO
# Marque como volumen las ventas de seis unidades o más y como menor todas las demás.
data['tipo_compra'] = np.where (data['quantity'] >= 6,'volumen','menor')
print(data['tipo_compra'].value_counts())
#Respuesta: o fue necesario recorrer las filas porque np.where() evalúa la condición 
#sobre toda la columna quantity y asigna automáticamente una categoría a cada fila.

# %%
# E. Agrupar para responder preguntas
# El patrón grupo → variable → operación
#Cada ejercicio de este bloque parte de una pregunta de negocio. Identifique primero 
#por qué variable
#se agrupa, sobre qué columna se calcula y qué operación resume el grupo.
# 12. ¿Cuánto ingreso genera cada sucursal? 
# Complete la agrupación que responde la pregunta.
resumen = (
    data
    .groupby('branch')['total']
    .sum()
)
print(resumen.round(2)) 

# %%
# 13. ¿Cuántas facturas registra cada método de pago? 
#Complete la columna sobre la que se cuenta y la operación correspondiente.
resumen = (
    data
    .groupby('payment')['invoice_id']
    .count()
)
print(resumen)
#Respuesta: Cada fila representa un método de pago y la cantidad 
#de facturas registradas con ese método.

# %%
# 14. Cada fila representa un método de pago y la cantidad de facturas 
# registradas con ese método.
resumen = (
    data
    .groupby('payment')
    .agg(
        facturas=('invoice_id', 'size'),
        unidades=('quantity', 'sum'),
        ingreso=('total', 'sum'),
    )
    .reset_index()
)
print(resumen.round(2))

# %%
# F. Integrar información
# Dos tablas que comparten una clave
# 15. Agregar la zona de cada sucursal 
# La tabla de ventas no indica en qué zona está cada sucursal. Esa información vive en
# un catálogo aparte. Intégrela conservando todas las ventas.
sucursales = pd.DataFrame({
    'branch': ['A', 'B', 'C'],
    'zona': ['Centro', 'Norte', 'Sur']
})
resultado = data.merge(
    sucursales,
    on='branch',
    how='left'
)
print(resultado.shape)
resultado[['branch', 'city', 'zona', 'total']].head()
#Respueta: Deben tener un dato en comun que permita relacionar los 2 registros

# %%
# Reto integrador
# Filtrar, agrupar, calcular, ordenar e interpretar
# 16. La sucursal líder entre los clientes Member 
#Considere únicamente las ventas de clientes de tipo Member. Determine qué sucursal
#genera el mayor ingreso total y cuál es su ticket promedio, entendido como el ingreso
#dividido entre el número de facturas. Escriba el código completo: aquí no hay espacios
#para completar.
# 1. Filtrar solamente los clientes Member
member = data[data['customer_type'] == 'Member']

# 2. Agrupar por sucursal
resumen = (
    member
    .groupby('branch')
    .agg(
        facturas=('invoice_id', 'size'),
        ingreso=('total', 'sum')
    )
    .reset_index()
)

# 3. Calcular el ticket promedio
resumen['ticket_promedio'] = resumen['ingreso'] / resumen['facturas']

# 4. Ordenar de mayor a menor ingreso
resumen = resumen.sort_values('ingreso', ascending=False)

# 5. Mostrar resultado
print(resumen.round(2))

#Respuesta: La sucursal C lidera entre los clientes Member, ya que presenta el mayor 
# ingreso total. Su ticket promedio es de 336.58 USD. 
# Comparado con las otras sucursales, su ticket promedio es mayor. 
