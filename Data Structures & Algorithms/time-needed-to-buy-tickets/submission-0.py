class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        idx = 0

        time = 0
        while True:
            time += 1
            tickets[idx] -= 1
            if tickets[idx] == 0:
                if idx == k:
                    return time
            idx = (idx + 1) % n
            while tickets[idx] == 0:
                idx = (idx + 1) % n

        return time