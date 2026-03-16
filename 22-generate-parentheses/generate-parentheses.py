class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate_progressive(current: str, opening_num: int, closing_num:int):
            nonlocal result
            if len(current)==2*n:
                result.append(current)
                return
            
            if opening_num<n:
                generate_progressive(current+'(', opening_num+1, closing_num)
            
            if closing_num<opening_num:
                generate_progressive(current+')', opening_num, closing_num+1)


        generate_progressive('', 0, 0)
        return result

        



        