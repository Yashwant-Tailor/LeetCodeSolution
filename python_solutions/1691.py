class Solution:
    def is_small(self,cube1,cube2,idx1,idx2):
        return cube1[idx1[1]] <= cube2[idx2[1]] and cube1[idx1[2]] <= cube2[idx2[2]] and cube1[idx1[0]] <= cube2[idx2[0]]
    def get_idx_group(self):
        res = []
        res.append((0,1,2))
        res.append((0,2,1))
        res.append((1,0,2))
        res.append((1,2,0))
        res.append((2,0,1))
        res.append((2,1,0))
        return res
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Solution Overview
        # first sort the cuboids (x[0]+x[1]+x[2]) as we know for sure that the possible candidate for which (x[0]+x[1]+x[2]) is bottom cube are only the cubes for which we have their total dimension sum less than the given dimension sum

        # Use dp to find the optimal answer 
        cuboids.sort(key=lambda x : (x[0]+x[1]+x[2]))
        stack = [{} for idx in range(len(cuboids))]
        for idx,cube in enumerate(cuboids):
            for idx_grp in self.get_idx_group():
                stack[idx][idx_grp] = cube[idx_grp[0]]
        for right_idx in range(len(cuboids)):
            for left_idx in range(0,right_idx):
                for r_idx_grp in self.get_idx_group():
                    for l_idx_grp in self.get_idx_group():
                        if self.is_small(cuboids[left_idx],cuboids[right_idx],l_idx_grp,r_idx_grp):
                            stack[right_idx][r_idx_grp] = max(stack[right_idx][r_idx_grp] , stack[left_idx][l_idx_grp] + cuboids[right_idx][r_idx_grp[0]])
        max_st_height = -1
        for stack_h in stack:
            for cube_h in stack_h.values():
                max_st_height = max(max_st_height,cube_h)
        return max_st_height
