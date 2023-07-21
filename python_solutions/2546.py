class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # Solution Overview
        # first let find the places where s[i] != t[i]
        # divide these indices into two groups 
        # group1 : indices where s[i] == 0 and t[i] == 1 (let say the count of such indices is n)
        # group2 : indices where s[i] == 1 and t[i] == 0 (let say the count of such indices is m)

        # if we have all the s[i] == 0 and there is some difference then it is not possible to make s == target
        is_all_zero = True
        diff_count = 0
        eq_1_idx = None
        not_eq_1_idx = None
        not_eq_0_idx = None
        for idx,char in enumerate(s):
            is_all_zero &= (s[idx] == '0')
            diff_count += 0 if s[idx] == target[idx] else 1
            if char == '1':
                if target[idx] == '1':
                    eq_1_idx = idx
                else:
                    not_eq_1_idx = idx
            else:
                if target[idx] == '1':
                    not_eq_0_idx = idx
        if is_all_zero and diff_count > 0:
            return False
        if is_all_zero and diff_count  == 0:
            return True
        # we have atleast '1' in s
        # this '1' could be at equal position (s[i] == t[i] == '1')
        # or it could be at not equal position (s[i] != t[i] and s[i] == '1' and t[i] == '0')
        if eq_1_idx is not None:
            # this 1 will make group1 indcies equal to target by considering eq_1_idx as i and group1 indices as j for our operations 
            # for group2 we will consider eq_1_idx as j and group2 indices as i for our operations
            return True
        else:
            # if we have any not_eq_0_idx then we can use the not_eq_1_idx to make not_eq_0_idx equal to target in one operation and after this we will use the '1' at index not_eq_0_idx to make all other character equal to target
            if not_eq_0_idx is not None:
                return True
        return False
            

