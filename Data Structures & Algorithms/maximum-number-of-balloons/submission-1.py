class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = defaultdict(int)
        min_leters = len(text) // 5
        for i in text:
           if i == 'b' or i == 'a' or i == 'l' or i == 'o' or i=='n':
                d[i] += 1
        return min(d['a'], d['b'], d['l'] // 2, d['o'] // 2, d['o'])
            









                
        '''l = [0]*5
        for i in text:
            if i == 'b':
                l[0] +=1
            if i == 'a':
                l[1] +=1
            if i == 'l':
                l[2] +=1
            if i == 'o':
                l[3] +=1
            if i == 'n':
                l[4] +=1
        '''
        