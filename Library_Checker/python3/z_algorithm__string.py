class ZArr:
    @staticmethod
    def cal(s:str)->list[int]:
        zval = [0]*len(s)
        zval[0] = len(s)
        left,right = 0,0
        for idx in range(1,len(s)):
            if idx < right:
                zval[idx] = min(zval[idx-left],right-idx)
            while idx + zval[idx] < len(s) and s[zval[idx]] == s[idx+zval[idx]]:
                zval[idx] += 1
            if idx + zval[idx] > right:
                right = idx + zval[idx]
                left = idx
        return zval
# s = input('Give input string\n')
s = input()
# print(f'Z array for the input string "{s}":')
print(*ZArr.cal(s))
