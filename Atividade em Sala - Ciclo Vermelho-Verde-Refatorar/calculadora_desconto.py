"""
Refatoração aplicando o Padrão de Projeto: STRATEGY
Participantes no domínio do problema:
- Strategy (Interface/Classe Abstrata): EstrategiaDesconto
- Concrete Strategies: DescontoNulo, DescontoPercentual, DescontoPorFaixa
- Context: CalculadoraDesconto
"""

from abc import ABC, abstractmethod


# Strategy Interface
class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor_total: float) -> float:
        pass


# Concrete Strategy 1
class DescontoNulo(EstrategiaDesconto):
    def calcular(self, valor_total: float) -> float:
        return valor_total


# Concrete Strategy 2
class DescontoPercentual(EstrategiaDesconto):
    def __init__(self, taxa: float):
        self.taxa = taxa

    def calcular(self, valor_total: float) -> float:
        return valor_total * (1 - self.taxa)


# Concrete Strategy 3
class DescontoPorFaixa(EstrategiaDesconto):
    def __init__(self, limite: float, desconto_fixo: float):
        self.limite = limite
        self.desconto_fixo = desconto_fixo

    def calcular(self, valor_total: float) -> float:
        if valor_total > self.limite:
            return valor_total - self.desconto_fixo
        return valor_total


# Context
class CalculadoraDesconto:
    def calcular(self, valor_total: float, tipo_desconto: str, taxa: float = 0.0, limite: float = 0.0, desconto_fixo: float = 0.0) -> float:
        # Mapeamento dinâmico para manter compatibilidade com a interface chamada pelos testes
        estrategias = {
            "SEM_DESCONTO": DescontoNulo(),
            "PERCENTUAL": DescontoPercentual(taxa),
            "FAIXA": DescontoPorFaixa(limite, desconto_fixo)
        }
        estrategia = estrategias.get(tipo_desconto, DescontoNulo())
        return estrategia.calcular(valor_total)


"""
===============================================================================
PASSO 3: AUTOAVALIAÇÃO
===============================================================================
1. Critérios Atingidos:
   - [X] Testes em arquivo separado do código de produção (3 variações).
   - [X] Histórico git com 3 commits (red, green, refactor).
   - [X] Commit da fase vermelha sem implementação de sucesso.
   - [X] Padrão Strategy aplicado e comentado com participantes nomeados.
   - [X] Suíte executa e passa 100% dos testes pós-refatoração.

2. Mudança na Estrutura do Código:
   Na fase 'green', a regra de negócio estava acoplada num encadeamento 'if/elif/else'
   dentro do método principal. Na fase de refatoração, o algoritmo de desconto foi
   extraído para classes independentes derivadas de 'EstrategiaDesconto'. Isso eliminou
   o acoplamento e permitiu extensão sem modificar a classe principal.

3. Parte que Deu Mais Trabalho:
   Manter a assinatura do método `calcular()` retrocompatível com a fase verde
   para que os testes não precisassem ser alterados durante a refatoração.
"""