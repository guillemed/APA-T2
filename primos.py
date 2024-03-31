
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