class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) -1
            nums[i] = -1*abs(nums[i])
        l = []
        for i in range(len(nums)):
            if nums[i]>0:
                l.append(i+1)
        return l


