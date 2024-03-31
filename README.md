# Segunda tarea de APA 2023: Manejo de números primos

## Nom i cognoms: Raul González Díaz y Guillermo Efrén Medina Guamán

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Escriba las funciones `mcmN()` y `mcdN()`, que calculan el mínimo común múltiplo y el máximo común divisor para un
número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcmN(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcdN(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.

<img src="test.png" width="640" align="center">

#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```python

def esPrimo(numero):
    """
    Devuelve *True* si su argumento es primo, y *False* si no lo es.
    
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """

    for prueba in range(2, int(numero**0.5)+1): 
        if numero%prueba == 0:
            return False
        
    return True

def primos(numero):
    """
    Devuelve una *tupla* con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """

    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])

def descompon(numero):
    """
    Devuelve una *tupla* con la descomposición en factores primos de su argumento.

    """
    lista=[] # lista vacia
    for factor in primos(numero):
        while numero%factor == 0:
            lista.append(factor)
            numero //= factor
    return tuple(lista)

def dicFact(numero1,numero2):
    """
    Devuelve el factor primo de un numero correspondiente, la funcion tiene 2 numeros como argumentos.

    >>> dicFact(90, 14)
    ({2: 1, 3: 2, 5: 1, 7: 0}, {2: 1, 3: 0, 5: 0, 7: 1})

    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)

    factores = set(factores1 + factores2)
    dic_fact1 ={factor: 0 for factor in factores}
    dic_fact2 ={factor: 0 for factor in factores}

    for factor in factores1: dic_fact1[factor] +=1
    for factor in factores2: dic_fact2[factor] +=1

    return dic_fact1, dic_fact2

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    
    >>> mcm(90, 14)
    630
    """

    mcm = 1
    dic_fact1, dic_fact2 = dicFact(numero1, numero2)
    for factor in dic_fact1 | dic_fact2:
        mcm *= factor**max(dic_fact1[factor], dic_fact2[factor])
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(924, 780)
    12

    """

    mcd = 1
    dic_fact1, dic_fact2 = dicFact(numero1, numero2)

    for factor in dic_fact1 | dic_fact2:
        mcd *= factor ** min(dic_fact1[factor], dic_fact2[factor])
    return mcd

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcmN(90, 14, 28, 35)
    1260

    """
    dicFactNumeros = [dicFact(numero, numero + 1) for numero in numeros] if len(numeros) > 1 else [dicFact(numeros[0])]
    factores = set() # conjunto vacío

    for dic_fact1, dic_fact2 in dicFactNumeros:
        factores.update(dic_fact1.keys()) 
        factores.update(dic_fact2.keys())
    mcmN = 1
    for factor in factores:
        mcmN *= factor ** max(dic_fact1.get(factor, 0) for dic_fact1, dic_fact2 in dicFactNumeros) 
        
    return mcmN

def mcdN(*numeros):
    """
   Devuelve el máximo común divisor de sus argumentos.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    dicFactNumeros = [dicFact(numero, numero + 1) for numero in numeros] if len(numeros) > 1 else [dicFact(numeros[0])]
    factores = set()
    for dic_fact1, dic_fact2 in dicFactNumeros:
        factores.update(dic_fact1.keys())
        factores.update(dic_fact2.keys())
    mcdN = 1
    for factor in factores:
        mcdN *= factor ** min(dic_fact1.get(factor, 0) for dic_fact1, dic_fact2 in dicFactNumeros) 
    return mcdN

import doctest
doctest.testmod()
```

#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
