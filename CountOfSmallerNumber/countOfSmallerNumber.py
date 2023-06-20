class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Função que será chamada recursivamente para ordenar as duas metades do array
        def Sort_and_Count(nums):
            # Calculando a metade do comprimento do array
            metade = len(nums) // 2
            # Se o array não for vazio
            if metade:
                # Aplicando a função recursivamente para cada metade do array
                esquerda, direita = Sort_and_Count(nums[:metade]), Sort_and_Count(nums[metade:])
                compPrimeiraMetade, compSegundaMetade = len(esquerda), len(direita)
                i = 0
                j = 0
                # Enquanto i for menor que o comprimento da esquerda ou 
                # j for menor que o comprimento da direita
                while i < compPrimeiraMetade or j < compSegundaMetade:
                    # Se todos os elementos da segunda metade já foram verificados
                    # ou o elemento atual da esquerda for menor ou igual ao atual da direita 
                    if j == compSegundaMetade or i < compPrimeiraMetade and esquerda[i][1] <= direita[j][1]:
                        # Colocando o elemento atual da esquerda na posição correta
                        nums[i+j] = esquerda[i]
                        contagem[esquerda[i][0]] += j
                        i += 1
                    else:
                        # Colocando o elemento atual da direita na posição correta
                        nums[i+j] = direita[j]
                        j += 1
            return nums

        # Inicializando o array contagem com 0 em todas as posições
        contagem = [0] * len(nums)
        # Criando uma lista de tuplas, onde cada uma contém valor e índice de cada elemento
        Sort_and_Count(list(enumerate(nums)))
        return contagem
