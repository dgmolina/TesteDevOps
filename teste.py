import pytest
from utilidades import multiplicacao, divisao


def teste_mult():
    assert multiplicacao(2,2) == 4
    assert multiplicacao(2,0) == 0
    assert multiplicacao(-1, 20) == -20
    assert multiplicacao(3,1.5) == 4.5

def teste_div():
    assert divisao(4,2) == 2
    assert divisao(5,2) == 2.5
    assert divisao(0, 10) == 0
    assert divisao(-10, 2) == -5
    assert divisao(10, -2) == -5 