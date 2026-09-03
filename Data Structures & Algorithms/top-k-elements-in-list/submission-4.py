class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        l = {}

        for i in nums:
            l[i] = l.get(i, 0) + 1

        sorted_keys = sorted(l, key=l.get, reverse=True)

        return sorted_keys[:k]