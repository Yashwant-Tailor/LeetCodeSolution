class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # we can place all the z type of string together 
        # ABABAB.....AB = A......B (length of this string will be z*2)
        # now if we have x == y then we can place 
        # AABBAABB...AABB = A....B (where AA and BB are in equal number)
        # length of this string will be x*2{length of AA} + y*2{length of BB} = x*4 (as x==y)
        #
        # other case we can have x != y
        # Without loss of generality assume x > y 
        # then we can place the string in 
        # AABBAABBAA...BBAA = A....A (where count of AA is one greater than BB)
        # length of this string will be (y+1)*2{length of AA}+ y*2 {length of BB}= y*4 + 2
        return z*2 + (min(x,y)*4 if x==y else min(x,y)*4 + 2)
