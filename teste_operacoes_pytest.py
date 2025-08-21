import operacoes
import pytest

def testar_soma():
    assert operacoes.soma(1,1) == 2
    assert operacoes.soma(-1,1) == 0

def testar_subtra():
    assert operacoes.subtra(2,1) == 1
    assert operacoes.subtra(-2,1) == -3


def testar_multip():
    assert operacoes.multip(3,9) == 27
    assert operacoes.multip(-3,9) == -27
    assert operacoes.multip(-3,-9) == 27
    assert operacoes.multip(0,9) == 0
    
def testar_dividir():
    assert operacoes.dividir(4,2) == 2
    assert operacoes.dividir(8,-2) == -4
    import pytest 
    with pytest.raises(ValueError):
        operacoes.dividir(1,0)

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-vv"]))