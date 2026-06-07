class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        k = len(strs)
        if k <= 1:
            return strs[0]

        common_pref = ""
        for i, c in enumerate(strs[0]):

            for j in range(1, k):
                if len(strs[j]) <= i or strs[j][i] != c:
                    return common_pref
            common_pref += c

        return common_pref
        

        