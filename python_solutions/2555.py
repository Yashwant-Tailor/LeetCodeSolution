class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # Solution Overview
        # for each position first calculate the number of prizes we can collect in between (poistion[i],position[i]+k)
        # now for each position we will pick the second interval optimally (it is clear that there is no point in picking overlapping interval)

        prize_collection_sz_k = []
        right_end = 0
        idx = 0
        curr_prize_collected = 0
        while idx < len(prizePositions):
            curr_pos = prizePositions[idx]
            while right_end < len(prizePositions) and prizePositions[right_end] <= curr_pos + k:
                curr_prize_collected += 1
                right_end += 1
            prize_collection_sz_k.append((curr_prize_collected,curr_pos))
            while idx < len(prizePositions) and curr_pos == prizePositions[idx]:
                curr_prize_collected -= 1
                idx += 1
        last_pos = prizePositions[-1] + k + 1
        # put one dummy value for selection of second interval 
        prize_collection_sz_k.append((0,last_pos))
        # start from end of prize_collection_sz_k and fix first interval start at the current position , we already know the prize collected for first interval and we will maintain the best second interval we could pick from already visited indices which are after (index+k)
        ans  = 0 
        idx = len(prize_collection_sz_k)-2
        second_interval_max_collection  = prize_collection_sz_k[-1][0]
        right_idx = len(prize_collection_sz_k)-1
        while idx >= 0:
            first_interval_prize_collection , first_interval_start = prize_collection_sz_k[idx]
            while right_idx > idx and prize_collection_sz_k[right_idx][1] > first_interval_start + k:
                second_interval_max_collection = max(second_interval_max_collection, prize_collection_sz_k[right_idx][0])
                right_idx -= 1
            curr_idx_prize_collection = first_interval_prize_collection + second_interval_max_collection
            ans = max(ans , curr_idx_prize_collection)
            idx -= 1
        return ans


