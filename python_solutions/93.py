class Solution:
    def is_valid_ip_num(self,ip_num):
        if ip_num == '':
            return False
        if ip_num[0] == '0' and len(ip_num) > 1:
            return False
        num = int(ip_num)
        return 0 <= num <= 255
    def is_valid_ip(self,ip_parts):
        is_valid = True
        for ip_part  in ip_parts:
            is_valid &= self.is_valid_ip_num(ip_part)
        return is_valid
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Solution Overview
        # perform three for loops to fix the location of dot ('.')

        n = len(s)
        ip_first_part = ''
        ans = []
        for i in range(n):
            ip_first_part += s[i]
            ip_second_part = ''
            for j in range(i+1,min(i+4,n)):
                ip_second_part += s[j]
                ip_third_part = ''
                for k in range(j+1 , min(j+4, n)):
                    ip_third_part += s[k]
                    ip_fourth_part = s[k+1:]
                    if self.is_valid_ip([ip_first_part,ip_second_part,ip_third_part,ip_fourth_part]):
                        valid_ip = ip_first_part + '.' + ip_second_part + '.' + ip_third_part + '.' + ip_fourth_part
                        ans.append(valid_ip)
        return ans
