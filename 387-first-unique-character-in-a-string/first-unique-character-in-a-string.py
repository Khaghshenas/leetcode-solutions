class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        min_index = {}
        not_repeated = {}

        for i, c in enumerate(s):
            if c not in not_repeated:
                not_repeated[c] = True
                min_index[c] = i
            else:
                not_repeated[c] = False

        min_i = float('inf') 
        for c in not_repeated:
            if not_repeated[c]==True:
                min_i = min(min_i, min_index[c])
        
        return min_i if min_i != float('inf') else -1


        