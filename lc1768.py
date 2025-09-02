class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1=''
        s2=''
        s3=''
        if len(word1)>len(word2):
            s1=word1[:len(word2)]
            s2=word2
            s3=word1[len(word2):]

        elif len(word2)>len(word1):
            s2=word2[:len(word1)]
            s1=word1
            s3=word2[len(word1):]

        else:
            s1=word1
            s2=word2

        result=''
        for i in range(len(s1)):
            result+=s1[i]+s2[i]

        result+=s3
        return result
