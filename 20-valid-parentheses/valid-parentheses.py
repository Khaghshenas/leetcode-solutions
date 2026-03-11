class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False

        stack = []
        pairs = {'(':')', '{':'}', '[':']'}

        for c in s:

            if c in pairs:
                stack.append(c)
                continue
            elif stack:
                c_1 = stack.pop()
                if pairs[c_1]==c:
                    continue
                else:
                    return False
            else:
                return False

        return not stack


        