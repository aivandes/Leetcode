class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx, num in enumerate(nums):
            if (target - num) in res:
                return [idx, res[target - num]]
            else:
                res[num] = idx
