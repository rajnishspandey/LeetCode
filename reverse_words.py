class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
                 
        return ' '.join(words)
        

obj = Solution()
result = obj.reverseWords("example   good a")
print(result)
