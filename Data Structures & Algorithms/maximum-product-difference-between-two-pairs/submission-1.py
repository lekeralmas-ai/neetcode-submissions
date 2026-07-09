class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_product = float('-inf')
        min_product = float('inf')
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Ensure distinct indices
                product = nums[i] * nums[j]
                max_product = max(max_product, product)
                min_product = min(min_product, product)
        
        return max_product - min_product