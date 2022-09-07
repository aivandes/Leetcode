class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = float("-inf")
        places = 0
        
        for i in range(len(nums)):
            if nums[i] > num:
                num = nums[i]
                places += 1

            else :
                nums[i] = float("inf")

        nums.sort()
        
        return places
