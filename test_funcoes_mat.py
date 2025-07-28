from funcoes_mat import dividir, subtrair, eh_par, raiz_quadrada, inverter_string

def test_dividir():
    assert dividir(9, 3) == 3

def test_subtrair():
    assert subtrair(6, 3) == 3

def test_eh_par():
    assert eh_par(10) is True
    assert eh_par(7) is False

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3
    assert raiz_quadrada(0) == 0

def test_inverter_string():
    assert inverter_string("python") == "nohtyp"
    assert inverter_string("abc") == "cba"
