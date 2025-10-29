class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        #MISSED THE CASE WHERE K > LEN(NUMS), FIX IT
        if k > len(nums):
            k=k%len(nums)

        if nums==[] or len(nums)==1:
            return

        p1=0
        p2=len(nums)-1
        while (p2-p1) > 0:
            nums[p1],nums[p2]=nums[p2],nums[p1]
            if (p2-p1) ==1:
                pass
            p1+=1
            p2-=1

        len1=k
        p1=0
        p2=k-1
        while (p2-p1) > 0:
            nums[p1],nums[p2]=nums[p2],nums[p1]
            if (p2-p1) ==1:
                pass
            p1+=1
            p2-=1

        len2=len(nums)-k
        p1=k
        p2=len(nums)-1
        while (p2-p1) > 0:
            nums[p1],nums[p2]=nums[p2],nums[p1]
            if (p2-p1) == 1:
                pass
            p1+=1
            p2-=1

        return













        #OLD SLOW ALGORITHM GOING OVER EACH PAIR FOR EACH ROTATION O(N*K)
        '''
        length=len(nums)
        i=-1
        void=nums[-1]

        if nums==[] or length==1:
            return

        while k!=0:
            try:
                nums[i]=nums[i-1]
                i-=1
            except:
                nums[i]=void
                void=nums[-1]
                k-=1
                i=-1
                continue'''

            #EVERY ITERATION CHECKS THIS BOOLEAN, THIS IS SLOW
        '''if i == -(length):
                k-=1
                nums[-length]=void
                void=nums[-1]
                i=-1'''    
        return        
                
