class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False

        stack = []
        opening = "({["
        closing = ")}]"
        for i, c in enumerate(s):

            if c in opening:
                stack.append(c)
                continue
            elif stack:
                c_1 = stack.pop()
                if c_1=='(' and c==')' or c_1=='{' and c=='}' or c_1=='[' and c==']':
                    continue
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True


        