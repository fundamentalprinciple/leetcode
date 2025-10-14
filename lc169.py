class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for element in nums:
            if element in dict.keys():
                dict[element]+=1
            else:
                dict[element]=1
        max=-float('inf')
        max_key=None
        for key in dict.keys():
            if dict[key] > max:
                max=dict[key]
                max_key=key
        return max_key        
