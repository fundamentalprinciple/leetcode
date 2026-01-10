class Solution:

    def countBits(self, n: int) -> List[int]:        
        #LINEAR SOLUTION
        result = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset*2 == i:
                offset = offset*2
            result[i] = 1 + result[i-offset]    
        return result    
        
        '''
        result = []
        for j in range(n+1):
            if len(Solution().mem.keys()) > j:
                result.append(Solution().mem[j])
            else:    
                count_ones = 0
                i = j
                while i != 0:
                    if i % 2 == 1:
                        count_ones += 1
                    i = i//2
                Solution().mem[j] = count_ones
                result.append(count_ones)
        return result
        '''

