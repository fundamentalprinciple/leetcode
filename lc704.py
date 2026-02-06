class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)-1
        p = b//2
        while(b-a>1):
            if nums[p] == target:
                return p
            elif nums[p] < target:
                a = p
                p = a + (b-a)//2
            else:
                b = p-1
                p = a + (b-a)//2
        if nums[a] == target:
            return a
        elif nums[b] == target:
            return b           
        return -1   

