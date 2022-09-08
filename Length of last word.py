class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = len(s)
        j = -1
        count_char = 0
        
        while abs(j) <= length and s[j] == " ":
            j -= 1
        
        while abs(j) <= length and s[j] != " ":
            count_char += 1
            j -= 1
        return count_char
