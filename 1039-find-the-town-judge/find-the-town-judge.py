class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        visited = set()

        for t in trust:
            visited.add(t[0])

        j = -1
        for i in range(1, n+1):
            if i not in visited:
                j = i
                break
        if j==-1:
            return -1

        trusting = set()
        for t in trust:
            if t[1]==j:
                trusting.add(t[0])
        
        for i in range(1, n+1):
            if i != j and (i not in trusting):
                return -1


        
        return j
        