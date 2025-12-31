class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        result = 0
        for i in range(1, len(nums)+1):
            result ^= i
        for i in nums:
            result ^= i
        return result        
        '''
        n = len(nums)
        sumN = 0
        sumR = int((n*(n+1))/2)
        for i in nums:
            sumN+=i
        return sumR-sumN        

