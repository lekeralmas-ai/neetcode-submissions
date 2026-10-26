class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        r_l = [0]* l
        l_r = [0] * l
        l_r[0] = nums[0]
        r_l[l-1] = nums[l-1]

        for i in range(1,l):
            l_r[i] = l_r[i-1]*nums[i]
            r_l[l-1-i] = r_l[l-i]*nums[l-1-i]
        res = [0]*l
        for i in range (l):
            if i == 0:
                res[i] = r_l[i+1]
            elif i == (l-1):
                res[i] = l_r[l-2]
            else:
                res[i] = l_r[i-1] * r_l[i+1]
        return res
        

