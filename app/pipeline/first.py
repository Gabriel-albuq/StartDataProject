"""Este módulo apenas de modelo."""


def first_function(a, b):
    """
    Essa função soma dois valores numéricos.

    Parâmetros:
    a (float ou int): Primeiro número a ser somado.
    b (float ou int): Segundo número a ser somado.

    Retorna:
    float ou int: A soma dos dois números, que pode ser um inteiro ou um número de ponto flutuante.
    """
    result = a + b

    return result


if __name__ == '__main__':
    num1 = 10
    num2 = 5

    valor = first_function(num1, num2)
    print(valor)
