def multiplicar(a, b):
    return(a * b)

def test_multiplicar_positiva():
    resultado = multiplicar(2, 3)
    esperado = 6
    assert resultado == esperado

def test_multiplicar_negativo():
    resultado = multiplicar(-2, -3)
    esperado = 6
    assert resultado == esperado

def test_multiplicar_zero():
    resultado = multiplicar(0, 0)
    esperado = 0
    assert resultado == esperado