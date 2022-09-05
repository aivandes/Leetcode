import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return x == 0
        else:
            num_digits = math.floor(math.log10(x)) + 1
            last_digit = 10**(num_digits - 1)
            
            for _ in range(num_digits // 2):
                
                if x // last_digit != x % 10:
                    return False
                
                x %= last_digit
                x //= 10
                
                
                last_digit //= 100
                
            else:
                return True
