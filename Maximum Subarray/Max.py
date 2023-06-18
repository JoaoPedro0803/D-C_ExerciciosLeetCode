from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Função auxiliar para calcular a soma máxima que pode ser obtida por uma subarray
        def divide_and_conquer(nums, i, j):
            if i == j - 1:
                return nums[i], nums[i], nums[i], nums[i]
            
            # dividimos a lista em duas metades
            mid = (i + j) // 2
            
            # recursivamente encontramos a soma máxima nas duas metades
            a1, m1, b1, s1 = divide_and_conquer(nums, i, mid)
            a2, m2, b2, s2 = divide_and_conquer(nums, mid, j)
            
            # a soma máxima do subarray que começa no início do array
            a = max(a1, s1 + a2)
            # a soma máxima do subarray que termina no final do array
            b = max(b2, s2 + b1)
            # a soma máxima do subarray que pode estar em qualquer lugar do array
            m = max(m1, m2, b1 + a2)
            # a soma total do array
            s = s1 + s2
            
            return a, m, b, s
        
        _, m, _, _ = divide_and_conquer(nums, 0, len(nums))
        return m
#https://leetcode.com/problems/maximum-subarray/description/