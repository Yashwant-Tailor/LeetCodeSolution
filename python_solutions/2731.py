class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        # Solution Overview
        # PART1:
        # if we know the final locations of robots after d seconds then calculating the distance between all pairs can be done in O(N LOGN) 
        # HOW : first sort the distance and then calculate the distance iteratevely for every pair in O(N)
        # PART2: How to get the final locations after d seconds ??
        # CASE1:
        # Let's first solve simple problem
        # what if the robots does not collide with each other even though they are
        # at the same coordinate at the same time
        # in this case the final location would be simply moving the robot in correct direction , so for ith robot final location would be nums[i] - d (if robot is moving in left direction , s[i]=='L') or nums[i] + d (if robot is moving in the right direction , s[i]=='R')
        # CASE2:
        # now let's consider that robot collision will occur , if you see closely the we can convert this case2 into case1 
        # let's say that robot at ith location has name 'ROBOT1' and robot at jth location has name 'ROBOT2' and these two will collide after some time (ROBOT1 is moving in right direction and ROBOT2 is moving in left direction)
        # after collision ROBOT1 will start moving in left direction and ROBOT2 will start moving in right direction
        # but if we interchange their name i.e. after collision ROBOT1 will be ROBOT2 and ROBOT2 will be ROBOT1 then we have that ROBOT1 will still be moving in right direction and ROBOT2 will still be moving in left direction
        # it is actually same as saying that there is no collision
        # which means that this case is equivalent to CASE1

        # Solution to CASE1
        # update the locations for each robot after d seconds
        for idx in range(len(nums)):
            nums[idx] += d * (-1 if s[idx] == 'L' else 1)
        # sort the locations
        nums.sort()
        ans = 0 
        curr_dis = 0
        MOD = int(1e9 + 7)
        # iteratevely calculate distance between every pair
        for idx , num in enumerate(nums):
            if idx == 0:
                curr_dis = 0
            else:
                curr_dis += idx * (nums[idx]-nums[idx-1])
                curr_dis %= MOD
            ans += curr_dis
            ans %= MOD
        return ans

