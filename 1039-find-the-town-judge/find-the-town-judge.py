class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1:
            return 1

        trusts = {i: [] for i in range(1, n + 1)}
        trusted = {i: 0 for i in range(1, n + 1)}

        for a, b in trust:
            trusts[a].append(b)
            trusted[b] += 1

        for i in range(1, n + 1):
            if not trusts[i] and trusted[i]==n-1:
                return i
        
        return -1