class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Solution Overview
        # if we close at jth hour then we need to know the number of indices before jth index (excluding this index) where we have customers[i] = 'N'
        # and after jth index (including the jth index) where we have customers[i] = 'Y'
        # to calculate this answer for every index we can precalculate the count and then iterate over the array to find the final answer

        right_y_cnt = 0
        left_n_cnt = 0
        for customer in customers:
            right_y_cnt += 1 if customer == 'Y' else 0
        final_pen = right_y_cnt
        closing_hour = 0
        for idx,customer in enumerate(customers):
            curr_pen = right_y_cnt + left_n_cnt
            if curr_pen < final_pen:
                final_pen = curr_pen
                closing_hour = idx
            left_n_cnt += 1 if customer == 'N' else 0
            right_y_cnt -= 1 if customer == 'Y' else 0
        if final_pen > left_n_cnt:
            final_pen = left_n_cnt
            closing_hour = len(customers)
        return closing_hour


