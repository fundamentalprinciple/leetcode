class Solution(object):
    def removeDuplicates(self, nums):
        main=0
        dup_list=[]
        dup_list.append(nums[main])
        max=nums[-1]
        k=0
        while nums[main]!=max:
            k+=1
            for index in range(len(nums[main+1:])):
                if not(nums[index+k] in dup_list):
                    nums[main+1],nums[index+k]=nums[index+k],nums[main+1]
                    dup_list.append(nums[main+1])
                    main+=1
                    break
        return k+1

