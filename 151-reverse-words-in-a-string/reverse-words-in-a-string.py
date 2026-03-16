class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current_word = ''

        for c in s:
            if c == ' ':
                if current_word:
                    words.append(current_word)
                    current_word = ''
            else:
                current_word += c

        if current_word:  # only append non-empty word
            words.append(current_word)

        return ' '.join(reversed(words))