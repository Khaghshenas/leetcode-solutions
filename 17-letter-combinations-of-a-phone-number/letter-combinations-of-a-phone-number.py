class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_to_str = {'1': "",
                      '2': "abc",
                      '3': "def",
                      '4': "ghi",
                      '5': "jkl",
                      '6': "mno",
                      '7': "pqrs",
                      '8': "tuv",
                      '9': "wxyz"}
        
        combinations_by_now = [""]

        for d in digits:
            new_combinations = []
            
            for comb in combinations_by_now:
                for c in num_to_str[d]:
                    new_combinations.append(comb + c)
            
            combinations_by_now = new_combinations
        

        return combinations_by_now