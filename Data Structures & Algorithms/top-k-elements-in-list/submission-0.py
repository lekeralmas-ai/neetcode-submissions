class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rew = list()
        times = list()
        for i in range(len(nums)):
            if nums[i] not in rew:
                rew.append(nums[i])
                times.append(1)
            else:
                times[rew.index(nums[i])] += 1
        pairs = list(zip(times, rew))
        pairs.sort(reverse=True)
        res = [pairs[i][1] for i in range(k)]
        return res