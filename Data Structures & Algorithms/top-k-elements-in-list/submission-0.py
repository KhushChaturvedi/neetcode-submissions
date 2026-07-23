class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        appearance = {}

        for num in nums:
            appearance[num] = appearance.get(num , 0) + 1

        pairs = []

        for key in appearance:
            pairs.append((appearance[key] , key))

        pairs.sort(reverse=True)

        result = []

        for i in range(k):
            result.append(pairs[i][1])

        return result
        