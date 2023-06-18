from typing import List, Optional

# Classe para definir o nó de uma lista vinculada. 
# Cada nó possui um valor e uma referência ao próximo nó.
class ListNode:
    def __init__(self, x):
        self.val = x  # Valor do nó
        self.next = None  # Referência ao próximo nó

class Solution:
    # Função principal para combinar todas as listas vinculadas.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # Se a lista de listas estiver vazia, retorne None.
            return None
        if len(lists) == 1:  # Se houver apenas uma lista vinculada, retorne essa lista.
            return lists[0]
        mid = len(lists) // 2  # Encontre o meio da lista de listas vinculadas.
        # Divida a lista de listas vinculadas em duas metades e as combine.
        left = self.mergeKLists(lists[:mid])  # Recursivamente combine a primeira metade das listas vinculadas.
        right = self.mergeKLists(lists[mid:])  # Recursivamente combine a segunda metade das listas vinculadas.
        # Combine as duas metades combinadas.
        return self.mergeTwoLists(left, right)

    # Função para combinar duas listas vinculadas.
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Crie um nó dummy. Este nó serve como a cabeça da lista vinculada combinada.
        current = dummy  # 'current' aponta para o último nó da lista vinculada combinada.
        # Enquanto houver elementos em ambas as listas vinculadas.
        while l1 and l2:
            # Se o valor na lista vinculada 1 é menor que o valor na lista vinculada 2.
            if l1.val < l2.val:
                current.next = l1  # Adicione o nó da lista vinculada 1 à lista vinculada combinada.
                l1 = l1.next  # Avance para o próximo nó na lista vinculada 1.
            else:
                current.next = l2  # Adicione o nó da lista vinculada 2 à lista vinculada combinada.
                l2 = l2.next  # Avance para o próximo nó na lista vinculada 2.
            # Avance para o próximo nó na lista vinculada combinada.
            current = current.next
        # Se ainda houver elementos na lista vinculada 1, adicione todos à lista vinculada combinada.
        if l1:
            current.next = l1
        # Se ainda houver elementos na lista vinculada 2, adicione todos à lista vinculada combinada.
        if l2:
            current.next = l2
        # Retorna a lista vinculada combinada, pulando o nó dummy.
        return dummy.next
    
    #https://leetcode.com/problems/merge-k-sorted-lists/description/
