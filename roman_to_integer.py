class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_num = {"I" :    1,
                        "V" :    5,
                        "X" :    10,
                        "L" :    50,
                        "C" :    100,
                        "D" :    500,
                        "M" :    1000} 
        if len(s) < 2:
            return roman_to_num[s] if s else -1
        
        curr = 0
        total = 0
        
        for i in s:
            previous = curr           
            curr = roman_to_num[i]
            total += curr
            
            if curr > previous:
                total -= (previous*2)
        return total
