def somar(a, b):
    return(a + b)

def test_soma_positiva():
    resultado = somar(2, 3)
    esperado = 5
    assert resultado == esperado

def test_soma_negativa():
    resultado = somar(-2, -3)
    esperado = -5
    assert resultado == esperado

def test_soma_zero():
    resultado = somar(0, 0)
    esperado = 0
    assert resultado == esperado