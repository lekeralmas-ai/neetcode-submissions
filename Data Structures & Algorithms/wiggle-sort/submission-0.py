class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = (len(nums) - 1) // 2
        # Create a new list with wiggle arrangement
        result = []
        # Take from the middle going backwards for smaller half
        # and from the end going backwards for larger half
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(nums[mid - i//2])
            else:
                result.append(nums[len(nums) - 1 - i//2])
        # Copy back to nums
        nums[:] = result
        