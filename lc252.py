"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def quickSort(arr):
    l = len(arr)
    if l == 1:
        return arr
    if l == 2:
        if arr[0].start < arr[1].start:
            return arr
        else:
            arr[0],arr[1]=arr[1],arr[0]    
            return arr    
    
    p = l//2
    a,b=0,0
    l1,l2=quickSort(arr[:p]),quickSort(arr[p:])
    flag = True
    while(flag):
        if l1[a].start <= l2[b].start:
            arr[a] == l1[a]
            if a == len(l1)-1:
                #FOR LOOP MAY BE REPLACABLE WITH SOME PYTHON METHOD
                for i in l2[b:]:
                    arr.append(i)
                flag = False
            else:
                a+=1    
        else:
            arr[b] = l2[b]
            if b == len(l2)-1:
                #FOR LOOP MAY BE REPLACABLE WITH SOME PYTHON METHOD
                for i in l1[a:]:
                    arr.append(i)
                flag = False
            else:
                b+=1
    return arr

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = len(intervals)
        if l < 2:
            return True

        intervals = quickSort(intervals)
        e,s=0,1
        while(s!=l):
            if intervals[e].end <= intervals[s].start:
                e+=1
                s+=1
                continue
            else:
                return False
        return True
