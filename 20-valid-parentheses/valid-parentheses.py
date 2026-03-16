class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        pairs = {'(': ')',
                 '{': '}',
                  '[': ']'}

        stack = []

        for c in s: 
            if c in pairs: # opening 
                stack.append(c)
            
            elif stack: # closing
                c_1 = stack.pop()
                if pairs[c_1]==c:
                    pass
                else:
                    return False
            else:
                return False
        
        
        return False if len(stack)>0 else True

            
        


        