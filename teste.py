import pytest
from utilidades import multiplicacao

def teste_mult():
    assert multiplicacao(2,2) == 4
    assert multiplicacao(2,0) == 0
    assert multiplicacao(-1, 20) == -20
    assert multiplicacao(3,1.5) == 4.5