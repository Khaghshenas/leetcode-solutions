#from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        #count = Counter(s)
        count = {}
        
        for i, c in enumerate(s):
            
            if c in count:
                x, idx = count[c]
                count[c] = (x+1, i)
            else:
                count[c] = (1, i)
        
        for c in count:
            x, idx = count[c]
            if x==1:
                return idx

        return -1

        