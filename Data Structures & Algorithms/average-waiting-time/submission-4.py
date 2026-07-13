class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = list()
        waiting_time.append(customers[0][1])
        for i in range(1,len(customers)):
            if customers[i][0] < customers[i-1][0] + waiting_time[i-1]:
                new_time = customers[i-1][0] + waiting_time[i-1]-customers[i][0]+customers[i][1]
                waiting_time.append(new_time)
            else:
                waiting_time.append(customers[i][1])
        return sum(waiting_time)/len(customers)

