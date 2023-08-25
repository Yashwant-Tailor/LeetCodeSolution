class Solution:
    def is_valid_expo(self,char):
        return (char == 'e') or (char == 'E')
    def is_digit(self,dig):
        return 0 <= (ord(dig) - ord('0')) <= 9
    def is_valid_sign(self,sign):
        return (sign == '+') or (sign == '-')
    def is_dot(self,char):
        return char == '.'
    def is_decimal(self,s):
        is_sign = None
        dot_cnt = 0
        idx = 0
        dig_cnt = 0
        while idx < len(s):
            if idx == 0 and self.is_valid_sign(s[idx]):
                is_sign = True
                idx += 1
            else:
                is_sign = False
            if idx < len(s):
                if self.is_dot(s[idx]):
                    dot_cnt += 1
                    idx += 1
                    continue
                if not self.is_digit(s[idx]):
                    return False
                else:
                    dig_cnt += 1
                idx += 1
        if is_sign is None:
            return False
        if dot_cnt != 1:
            return False
        return dig_cnt > 0
    def is_integer(self,s):
        is_sign = None
        idx = 0
        dig_cnt = 0
        while idx < len(s):
            if idx == 0 and self.is_valid_sign(s[idx]):
                is_sign = True
                idx += 1
            else:
                is_sign = False
            if idx < len(s):
                if not self.is_digit(s[idx]):
                    return False
                else:
                    dig_cnt += 1
                idx += 1
        if is_sign is None:
            return False
        return dig_cnt > 0
    def is_valid_expo_comp(self,s):
        if s == "NO_EXPONENT":
            return True
        return self.is_integer(s[1:])
            
    def get_comp1(self,s,idx):
        comp = ''
        idx = 0
        while idx < len(s) and not self.is_valid_expo(s[idx]):
            comp += s[idx]
            idx += 1
        return comp,idx

    def get_comp(self,s):
        comp1,idx1 = self.get_comp1(s,0)
        if idx1 == len(s):
            comp2 = "NO_EXPONENT"
        else:
            comp2 = s[idx1:]
        return comp1,comp2
    def isNumber(self, s: str) -> bool:
        # Solution Overview
        # just handle every edge cases
        # here comp1 = Decimal , Integer
        # comp2 = 'e', 'E'
        # comp3 = Integer
        comp1,comp2 = self.get_comp(s)
        if (not self.is_integer(comp1)) and (not self.is_decimal(comp1)):
            return False
        if not self.is_valid_expo_comp(comp2):
            return False
        return True
