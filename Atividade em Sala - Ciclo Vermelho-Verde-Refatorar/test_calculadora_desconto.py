"""
    1. Problema Escolhido:
    Calculadora de descontos para um e-commerce.

    2. Casos de Teste (Variações de Comportamento):
    - Variação 1: Cliente Sem Desconto (retorna o valor original do carrinho).
    - Variação 2: Desconto Percentual Direto (aplica X% no valor total).
    - Variação 3: Desconto por Faixa de Valor (ex.: R$ 50 de desconto para compras acima de R$ 300).

    3. Padrão de Projeto Escolhido:
    Strategy.
    Porquê: Permite isolar diferentes regras/algoritmos de desconto em classes
    separadas sem alterar a classe principal da Calculadora (cumprindo o Princípio do Aberto/Fechado).

    4. Estimativa do Tempo por Fase:
    - Red: 10 minutos
    - Green: 15 minutos
    - Refactor: 40 minutos
    - Ajustes/Autoavaliação: 15 minutos
"""

import pytest
from calculadora_desconto import CalculadoraDesconto


def test_cliente_sem_desconto():
    calc = CalculadoraDesconto()
    assert calc.calcular(valor_total=100.0, tipo_desconto="SEM_DESCONTO") == 100.0


def test_desconto_percentual():
    calc = CalculadoraDesconto()
    # 10% de desconto em 200.0 = 180.0
    assert calc.calcular(valor_total=200.0, tipo_desconto="PERCENTUAL", taxa=0.10) == 180.0


def test_desconto_por_faixa():
    calc = CalculadoraDesconto()
    # Se valor > 300, desconta 50. Valor = 400.0 -> Resulta em 350.0
    assert calc.calcular(valor_total=400.0, tipo_desconto="FAIXA", limite=300.0, desconto_fixo=50.0) == 350.0