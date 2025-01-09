from app.pipeline import (
    first_function,  # Ajuste para o nome correto do seu arquivo principal
)


# Teste a soma de dois números inteiros
def test_sum_integers():
    assert first_function(10, 5) == 15


# Teste a soma de dois números de ponto flutuante
def test_sum_floats():
    assert first_function(10.5, 5.5) == 16.0


# Teste a soma de um número inteiro e um número de ponto flutuante
def test_sum_int_and_float():
    assert first_function(10, 5.5) == 15.5


# Teste a soma de números negativos
def test_sum_negative_numbers():
    assert first_function(-10, 5) == -5


# Teste a soma de zero com outro número
def test_sum_zero():
    assert first_function(0, 5) == 5