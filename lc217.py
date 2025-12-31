class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            dict[i]=0

        for i in nums:
            if dict[i]==0:
                dict[i]+=1
            else:
                return True  
        return False     

