import operacoes

def test_somar():
    assert operacoes.somar(2, 3) == 5

def test_subtrair():
    assert operacoes.subtrair(5, 2) == 3

def test_multiplicar():
    assert operacoes.multiplicar(3, 4) == 12