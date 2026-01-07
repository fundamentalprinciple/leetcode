def sumPrefix(list, end):
        s = 0
        for i in list[0:end]:
            s += i
        return s

class NumArray:
    arr = []
    sums = []
    def __init__(self, nums: list[int]):
        self.arr = nums
        self.sums = []
        #MEMOIZING PREFIX SUBARRAY SUMS
        for i in range(len(self.arr)):
            self.sums.append(sumPrefix(self.arr, (i+1)))
        return

    def sumRange(self, left: int, right: int) -> int:
        '''
        #NAIVE O(N) TIME, O(1) Memmory
        sum = 0
        for i in self.arr[left:right+1]:
            sum+=i
        return sum
        '''
        #NEED TO FIX ALL THIS HARDCODING
        if len(self.arr) == 1:
            return self.arr[0]
        if left == right:
            return self.arr[left]
        if left == 0:
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
