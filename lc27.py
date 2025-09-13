class Solution(object):
    def removeElement(self, nums, val):
        nums_copy=[]
        for i in nums:
            nums_copy.append(i)

        index=-1
        for i in nums_copy:
            index+=1
            if i==val:
                nums.pop(index)
                index-=1
        k=len(nums)
        return k
