class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return Solution().climbStairs(n-1) + Solution().climbStairs(n-2)        
        
        O(2^N) TOO SLOW
        '''
        one, two = 1 , 1
        for i in range(n-1):
            one, two = one+two , one
        return one  
