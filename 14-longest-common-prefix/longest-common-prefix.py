class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common_pre = ""

        for i, c in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return common_pre
            common_pre += c

        return common_pre
        