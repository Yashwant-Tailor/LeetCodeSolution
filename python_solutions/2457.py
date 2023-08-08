class Solution:
    def get_dig_sum(self,num):
        res = 0
        while num > 0:
            res += num%10
            num //= 10
        return res
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # Solution Overview
        x = ''
        while self.get_dig_sum(n) - target > 0:
            curr_dig = n%10
            n //= 10
            add = 10 - curr_dig
            if add < 10:
                x += str(add)
                n += 1
            else:
                x += '0'
        if x == '':
            return 0
        return int(x[::-1])
