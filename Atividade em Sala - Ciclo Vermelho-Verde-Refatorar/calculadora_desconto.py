class CalculadoraDesconto:
    def calcular(self, valor_total, tipo_desconto, taxa=0.0, limite=0.0, desconto_fixo=0.0):
        if tipo_desconto == "SEM_DESCONTO":
            return valor_total
        elif tipo_desconto == "PERCENTUAL":
            return valor_total * (1 - taxa)
        elif tipo_desconto == "FAIXA":
            if valor_total > limite:
                return valor_total - desconto_fixo
            return valor_total
        return valor_total