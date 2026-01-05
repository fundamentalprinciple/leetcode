#NAIVE:
class NumArray:
    arr = []
    def __init__(self, nums: List[int]):
        self.arr = nums
        return 

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in self.arr[left:right+1]:
            sum+=i
        return sum    

 #MEMOIZED:
            #TOMMOROW
