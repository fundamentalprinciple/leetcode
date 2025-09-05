class Solution(object):
    #two pointers approach, not optimized for memmory
    def merge(self, nums1, m, nums2, n):
        p1,p2,l=0,0,[]
        while p1!=m and p2!=n:
            if nums1[p1]<=nums2[p2]:
                l.append(nums1[p1])
                p1+=1
            else:
                l.append(nums2[p2])
                p2+=1
        if p1==m:
            while p2!=n:
                l.append(nums2[p2])
                p2+=1
        elif p2==n:
            while p1!=m:
                l.append(nums1[p1]) 
                p1+=1       
        #mutating nums1 now:
        k=-1
        for i in l:
            k+=1
            nums1[k]=i  

        return                      
