class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Como é desejado o k-ésimo maior elemento, transforma o k em relação ao tamanho do array
        return self.exotericSelect(nums, len(nums) - k)
    
    def exotericSelect(self, nums: List[str], k: int) -> str:
        # Se o array tem apenas um elemento, retorne esse elemento
        if len(nums) == 1:
            return nums[0]
        
        # Obtendo um bom pivô a partir do algoritmo de mediana das medianas
        pivo = self.medianaDasMedianas(nums)
        
        # Dividindo os números em torno do pivô
        # Como os números estão como strings, usa-se a função int() para comparar os valores
        menoresQuePivo = [i for i in nums if int(i) < int(pivo)]
        maioresQuePivo = [i for i in nums if int(i) > int(pivo)]
        iguaisPivo = [i for i in nums if i == pivo]
        
        # Selecione qual partição buscar
        if k < len(menoresQuePivo):
            # Se k é menor que o número de elementos na partição de menoresQuePivo, vá para a esquerda
            return self.exotericSelect(menoresQuePivo, k)
        elif k < len(menoresQuePivo) + len(iguaisPivo):
            # Se k é menor que o número de elementos em menoresQuePivo + iguaisPivo, então o pivô é a resposta
            return iguaisPivo[0]
        else:
            # Caso contrário, vá para a direita
            return self.exotericSelect(maioresQuePivo, k - len(menoresQuePivo) - len(iguaisPivo))
    
    # Função para calcular a mediana das medianas
    def medianaDasMedianas(self, nums: List[str]) -> str:
        # Divida o array em sub-arrays de tamanho até 5.
        subarrays = [nums[j:j+5] for j in range(0, len(nums), 5)]
        
        # Para cada sub-array, obtem a mediana
        # Como os números estão como strings, usa-se a função int() para ordená-los
        medianas = [sorted(subarray, key=int)[len(subarray)//2] for subarray in subarrays]
        
        # Se o array de medianas tem 5 elementos ou menos, a mediana das medianas é a mediana do array de medianas
        if len(medianas) <= 5:
            return sorted(medianas, key=int)[len(medianas)//2]
        else:
            # Caso contrário, a mediana das medianas é a mediana do array de medianas das medianas
            return self.medianaDasMedianas(medianas)
