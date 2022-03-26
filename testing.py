import Examen1;
import pytest;

#########################################################

def test_pregunta_1():
    assert Examen1.numeroHermano(20) == True
    
def test_pregunta_2():
    assert Examen1.numeroHermano(8) == False
    
def test_pregunta_3():
    assert isinstance(str(Examen1.numeroHermano(-8)), str) == isinstance("Error en la entrada", str)
    
#########################################################

def test_pregunta_4():
    assert Examen1.numeroPolimax(4312) == True 
    
def test_pregunta_5():
    assert Examen1.numeroPolimax(327017) == True
    
def test_pregunta_6():
    assert Examen1.numeroPolimax(-6887) == False
    
def test_pregunta_7():
    assert Examen1.numeroPolimax(-99) == True
    
def test_pregunta_8():
    assert Examen1.numeroPolimax(7) == False
    
#########################################################    

def test_pregunta_9():
    assert Examen1.construirNumero([2, 3, 5, "Casa", 15, 9, 58.5, 9, 6, 4])  == 3863

def test_pregunta_10():
    assert Examen1.construirNumero([2, 13, 25, "Hola", 5, 4]) == 29

def test_pregunta_11():
    assert Examen1.construirNumero([2.3, 13, 25, "Hola", 455, 40]) == 0
    
#########################################################    

def test_pregunta_12():
    assert Examen1.encriptarClave(125689) == 906615

def test_pregunta_13():
    assert Examen1.encriptarClave(-125689) == -906615
    
def test_pregunta_14():
    assert isinstance(str(Examen1.encriptarClave(125)), str) == isinstance("Error: La cantidad de digitos no está entre 4 a 8", str)
