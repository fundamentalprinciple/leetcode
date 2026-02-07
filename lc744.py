class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a,b=0,len(letters)-1
        p=len(letters)//2
        while(b-a>1):
            if letters[p] <= target:
                a = p
                p = a + (b-a)//2
            else:
                b = p
                p = a + (b-a)//2
        if letters[a] > target:
            return letters[a]
        elif letters[b] > target:
            return letters[b]                 
        return letters[0]             
