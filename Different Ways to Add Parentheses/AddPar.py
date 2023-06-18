from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Caso base: se a expressão é um número, retorne o número em uma lista
        if expression.isdigit():
            return [int(expression)]

        res = [] # inicializa a lista de resultados
        # Percorremos a expressão
        for i, c in enumerate(expression):
            # Se o caractere é um operador...
            if c in ['-', '+', '*']:
                # Dividimos a expressão em duas partes baseadas no operador
                left = self.diffWaysToCompute(expression[:i]) # a parte esquerda da expressão
                right = self.diffWaysToCompute(expression[i+1:]) # a parte direita da expressão
                # Conquistamos resolvendo cada metade do problema
                # e depois combinamos os resultados para obter o resultado final
                for l in left:
                    for r in right:
                        # dependendo do operador, executamos a operação adequada
                        if c == '-':
                            res.append(l - r)
                        elif c == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)
        # retorne todos os resultados possíveis
        return res
