class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        # use dictionary to keep track of marble locations

        marble_locs = {} # key will be location and value will be the count of marbles at this location

        # add initial positions of marbles
        for marble_loc in nums:
            if marble_loc in marble_locs:
                marble_locs[marble_loc] += 1
            else:
                marble_locs[marble_loc] = 1
        # perform the steps 
        for step_idx, move_from in enumerate(moveFrom):
            move_to = moveTo[step_idx]
            marble_count = marble_locs[move_from]
            marble_locs[move_from] = 0
            if move_to in marble_locs:
                marble_locs[move_to] += marble_count
            else:
                marble_locs[move_to] = marble_count
        ans = []
        for key , value in marble_locs.items():
            if value > 0:
                ans.append(key)
        ans.sort()
        return ans
