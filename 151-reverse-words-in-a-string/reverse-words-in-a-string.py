class Solution:
    def reverseWords(self, s: str) -> str:

        words = []
        current_word = ''

        for c in s:
            if c==' ' and not current_word:
                continue
            elif c==' ' and current_word:
                words.append(current_word)
                current_word = ''
            else:
                current_word += c
        
        if current_word:
            words.append(current_word)

    
        sentence = ' '.join(reversed(words))
        return sentence
        