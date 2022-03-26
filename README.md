# 2022 Semestre 1
# Primer Examen

## Instrucciones Generales
- El archivo **debe** llamarse **Examen1.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- **Debe** contruir las funciones con **Python**
- **Debe** utilizar la programación vistas en clases **while for if elif**
- **Debe** crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**

## numeroHermano(num)
Escriba un programa con sintaxis Python cuya función principal se llame **numeroHermano(num)**, que reciba como entrada un número **entero positivo** denominado **num** y que retorne si cumple (True) o no los requisitos (False) de número hermano. 
- Un número hermano es un número natural y que poseer **dos divisores primos** 
- El uno no es primo, y no se tomará en cuenta el mismo **num**:
- Debe de agregar el código para números primos

Ejemplos del comportamiento de la función:
```python
>>> numeroHermano(20) #(divisores propios: 2, 4, 5, 10)
True
>>> numeroHermano (8) #(divisores propios: 2, 4)
False
>>> numeroHermano (-8)
“Error en la entrada”
```

## numeroPolimax(num)
Escriba un programa con sintaxis Python cuya función principal se llame **numeroPolimax(num)**, puede recibe un **número entero cualquiera** e indique si el número es un Número Polimax. 
- Un número es **Polimax** si al partir en dos el número, ambas partes tienen la misma cantidad de impares y pares. 
- La longitud del número debe ser par

Sea el número 4312, al partir este numero, generará 43 y 12
43 tiene 1 dígito par y 1 digito impar
12 tiene 1 dígito par y 1 digito impar
Tanto el 43 y 12 tiene la misma cantidad de dígitos pares e impares, por lo que la respuesta es **True**

Ejemplos del comportamiento de la función:
```python
>>> numeroPolimax (4312) # 43 y 12
True 
>>> numeroPolimax (327017) # 327 y 017
True
>>> numeroPolimax (-6887) # 68 87
False
>>> numeroPolimax (-99) # 99
True
>>> numeroPolimax (7) 
False
```

## construirNumero(lista)
Escriba un programa con sintaxis Python cuya función principal se llame **construirNumero(lista)**, puede recibe una **lista de elementos cualquiera**.
- Los números a tomar en cuenta son mayores a cero y menor a 10
- Primero debe separar en dos listas, aquellos números pares enteros positivos y en otra lista los números impares enteros positivos
- Con cada una de las listas construir un nuevo número
- Y finalizar sumándolos
- Prohibido el uso de **str()** y **int()**

Ejemplo:
1) lista = [2, 3, 5, "Casa", 15, 9, 58.5, 9, 6, 4]
2) pares = [2, 6, 4],  impares = [3, 5, 9, 9]
3) numeroPar = 264,  numeroImpar = 3599
4) 264 + 3599 = 3863

```python
>>> construirNumero([2, 3, 5, "Casa", 15, 9, 58.5, 9, 6, 4])  #pares = [2, 6, 4],  impares = [3, 5, 9, 9]
3863
>>> construirNumero([2, 13, 25, "Hola", 5, 4]) #pares = [2, 4],  impares = [5]
29
>>> construirNumero([2.3, 13, 25, "Hola", 455, 40]) #pares = [],  impares = []
0
```
## encriptarClave(num)
Escriba un programa con sintaxis Python cuya función principal se llame **encriptarClave(num)**, el número **num** debe ser entero diferente a cero, puede ser positivo o negativo. El número debe tener la cantidad desde 4 a 8 dígitos
Para encriptar una clave, se debe realizar los siguientes pasos:
1) Verificar que el número tenga el largo de digitos definido
2) Si el número es negativo, pasarlo a positivo
3) Transformar ese número a una base 7
4) Posteriormente restar el nuevo número base 7 menos el parámetro **num**
5) Si el parámetro **num** es negativo, la respuesta debe ser negativo

Ejemplo:
Sea num = 125689
Su cantidad de dígitos es 6 entonces está dentro del rango de 4 a 8
125689 as base 7 = 1032304
1032304 - 125689 = 906615

```python
>>> encriptarClave(125689)
906615
>>> encriptarClave(-125689)
-906615
>>> encriptarClave(125)
"Error: La cantidad de digitos no está entre 4 a 8"
```
