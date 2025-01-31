"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS , countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)
        return countS == countT
    
obj = Solution()
print(obj.isAnagram("rat","cat"))