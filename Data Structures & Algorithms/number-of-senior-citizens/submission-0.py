class Solution:
    def countSeniors(self, details: List[str]) -> int:
      sum = 0
      for ppl in details:
        if int(ppl[11] + ppl [12]) > 60 :
            sum +=1
      return sum