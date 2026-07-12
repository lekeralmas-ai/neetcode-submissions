class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        s = Counter(students)
        for sandwich in sandwiches:
            if s[sandwich] > 0:      
                s[sandwich] -= 1
                count += 1
            else:                     
                break
        return len(students) - count  
