# 2021 Semestre 2
# Primer Examen

## Instrucciones Generales
- El archivo **debe** llamarse **Examen1.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación **recursiva de pila**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**

##	Número abundante (25 puntos) 
Escriba un programa con sintaxis Python cuya función principal se llame **numeroAbundante(num)**, que reciba como entrada un número entero positivo denominado **num** y que retorne si cumple (True) o no los requisitos (False) de número abundante. 
Un número abundante es un número natural y que la suma de sus divisores es mayor que su duplo, es decir:
-	El valor de **num** será 12 y sus divisores son (1,2,3,4,6 y 12)
-	La suma de ellos son 1+2+3+4+6+12 = 28
-	Entonces el 12 es un número abundante porque la suma de sus divisores 28 y es mayor que el duplo de 12, es decir 24. (28 > 12 x 2)

```python
>>>numeroAbundate(12)
True
>>> numeroAbundate (8)
False
>>> numeroAbundate (-8)
“Error: La entrada, debe ser número positivo”
```

##	Suma Adyacentes Impar (25 puntos) 

Escriba un programa con sintaxis Python cuya función principal se llame **adyacentesImpares(num)**, recibe un número **entero positivo** y debe retornar **True** en caso de que todas las sumas de **dos dígitos adyacentes sean impares**, retornar **False** en caso de que alguna suma de adyacentes **no sea impar**, es decir:
- Sea num = 9252783
  - Agrupar cada 2 dígitos y sumarlos cada uno de ellos: 3+8, 7+2, 5+2, 9 y el resultado de cada una de esas suma son: 11, 9, 7, 9
  - Como se puede apreciar todos esos resultados son impares, por lo tanto la respuesta es **True**

```python
>>> adyacentesImpares (9252783) 
True 
>>> adyacentesImpares (51730)
False
>>> adyacentesImpares (5836)
True
>>> adyacentesImpares (-9)
“Error: Número debe ser positivo”
```

## Convertir Número (25 puntos) 

Escribir un programa con sintaxis Python cuya función principal se llame **convertirNumero(num, exponente)**, reciben dos números **enteros cualquiera** y retorne un nuevo número con la siguiente lógica:
- Sea el número num = 12558 y exponente = 4
- El total de dígitos de **num** debe ser **IMPAR**
- Se obtiene el dígito del medio (5) y aplica la potencia según su **exponente** es decir, 5 ** 4 = 625
- El extremo izquierdo (12) formará un nuevo número solo con los dígitos **impares**, es decir 1
- El extremo derecho (58) formará un nuevo número solo con los dígitos **pares**, es decir 8
- El nuevo número a formar sería el siguiente: 16258
- En el caso de no existir pares o impares, el resultado será de CERO

```python
>>> convertirNumero(12558, 4)
16258
>>> convertirNumero(-94161, 5) #-9 1 6
-916
>>> convertirNumero(8517210, 5) #51 16807 20
511680720
>>>convertirNumero('8517210', 5)
“Error: Debe ser entero”
```
  
##	Comprimir Número (25 puntos) 
Escriba un programa con sintaxis Python cuya función principal se llame **comprimirNumero(num)**, recibe un número **entero** y debe retornar un nuevo número quitando aquellos dígitos **repetidos** en este, es decir:
- Sea num = 15532, el **dígito 5** se aparece más de una vez por lo tanto será eliminado, dando como resultado, **1532**
- Sea num = 82581534, los **dígitos 8 y 5** se aparecen más de una vez por lo tanto serán eliminados, dando como resultado, **825134**

```python
>>> comprimirNumero (15532) 
1532 
>>> comprimirNumero (82581534) 
281534
>>> comprimirNumero (-82581534) 
-281534
>>>comprimirNumero('82581534')
“Error: Debe ser entero”
```
