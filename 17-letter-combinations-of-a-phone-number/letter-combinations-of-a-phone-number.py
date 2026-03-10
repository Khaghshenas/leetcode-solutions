class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {"1": "", 
                    "2": "abc", 
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        
        combinations_by_now = [""]
        
        for digit in digits:
            new_combinations = []
            for comb in combinations_by_now:
                for l in num_map[digit]:
                    new_combinations.append(comb+l)
            combinations_by_now = new_combinations

        return combinations_by_now
            
            