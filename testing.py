import Examen1;
import pytest;
    
def test_numeroAbundate_1():
    assert Examen1.numeroAbundante(12) == True
def test_numeroAbundate_2():
    assert Examen1.numeroAbundante(8) == False
def test_numeroAbundate_3():
    assert isinstance(Examen1.numeroAbundante(-8), str) == isinstance("Error: La entrada, debe ser número positivo", str)    
    
#############################################################################################

def test_adyacentesImpares_1():
    assert Examen1.adyacentesImpares (9252783) == True 
    
def test_adyacentesImpares_2():
    assert Examen1.adyacentesImpares (51730) == False
    
def test_adyacentesImpares_3():
    assert Examen1.adyacentesImpares (5836) == True
    
def test_adyacentesImpares_4():
    assert isinstance(Examen1.adyacentesImpares (-9), str) == isinstance("Error: Número debe ser positivo", str)
    
#############################################################################################

def test_convertirNumero_1():
    assert Examen1.convertirNumero(12558, 4) == 16258
def test_convertirNumero_2():
    assert Examen1.convertirNumero(-94161, 5) == -916
def test_convertirNumero_3():
    assert Examen1.convertirNumero(8517210, 5) == 511680720
def test_convertirNumero_4():
    assert isinstance(Examen1.convertirNumero('8517210', 5), str) == isinstance("Error: Debe ser entero", str)    
    
#############################################################################################

def test_comprimirNumero_1():
    assert Examen1.comprimirNumero (15532) == 1532 
def test_comprimirNumero_2():
    assert Examen1.comprimirNumero (82581534) == 281534
def test_comprimirNumero_3():
    assert Examen1.comprimirNumero (-82581534) == -281534    
def test_comprimirNumero_4():
    assert isinstance(Examen1.comprimirNumero('82581534'), str) == isinstance("Error: Debe ser entero", str)     
