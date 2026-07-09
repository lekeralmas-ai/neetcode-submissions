class Solution:
    def minOperations(self, s: str) -> int:
        # Try both alternating patterns
        count_start_with_0 = 0  # Pattern: 0,1,0,1,...
        count_start_with_1 = 0  # Pattern: 1,0,1,0,...
        
        for i in range(len(s)):
            # Pattern starting with '0'
            expected_0 = '0' if i % 2 == 0 else '1'
            if s[i] != expected_0:
                count_start_with_0 += 1
            
            # Pattern starting with '1'
            expected_1 = '1' if i % 2 == 0 else '0'
            if s[i] != expected_1:
                count_start_with_1 += 1
        
        return min(count_start_with_0, count_start_with_1)