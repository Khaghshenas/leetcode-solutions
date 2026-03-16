class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        current = ""

        def generate(current: str, opening_count: int, closing_count: int):
            if len(current)==2*n:
                result.append(current)
                return

            if opening_count<n:
                generate(current+'(', opening_count + 1, closing_count)
            if closing_count<opening_count:
                generate (current+')', opening_count, closing_count+1)
            

        generate('', 0, 0)
        return result

        



        