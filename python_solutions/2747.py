class Solution:
    class QUERY:
        def __init__(self, start, end, idx):
            self.query_start = start
            self.query_end = end
            self.query_idx = idx
            self.query_ans = 0

        def get_query_start(self):
            return self.query_start

        def get_query_end(self):
            return self.query_end

        def set_query_ans(self, ans):
            self.query_ans = ans

        def get_query_ans(self):
            return self.query_ans

        def get_query_idx(self):
            return self.query_idx

    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Solution Overview
        # sort the queries array and maintain a dictionary to keep track of unique elements in
        # range [quries[i]-x, quries[i]]

        query_arr = []
        for idx, query in enumerate(queries):
            query_arr.append(self.QUERY(query - x, query, idx))
        # sort query_arr according to start_time
        query_arr.sort(key=lambda x: x.get_query_start())
        # sort the logs with time
        logs.sort(key=lambda x: x[1])

        # two pointer to keep track of logs added in the [curr_interval_start,curr_interval_end]
        curr_interval_start = 0
        curr_interval_end = 0
        # dictionary to keep track of unique elements in [curr_interval_start,curr_interval_end]
        unique_server_ids = {}

        # iterate over query_arr
        for query in query_arr:
            # traverse elements from till we have logs[curr_interval_end][1] <= query_end
            while curr_interval_end < len(logs) and logs[curr_interval_end][1] <= query.get_query_end():
                # decrease the count and remove if possible, the server_id from unique_server_id
                server_id = logs[curr_interval_end][0]
                if server_id in unique_server_ids:
                    unique_server_ids[server_id] += 1
                else:
                    unique_server_ids[server_id] = 1
                curr_interval_end += 1
            # add the server ids till we have logs[curr_idx][curr_interval_start] < query_start
            while curr_interval_start < len(logs) and logs[curr_interval_start][1] < query.get_query_start():
                server_id = logs[curr_interval_start][0]
                if server_id in unique_server_ids:
                    unique_server_ids[server_id] -= 1
                    if unique_server_ids[server_id] == 0:
                        unique_server_ids.pop(server_id)
                curr_interval_start += 1
            # answer for this query will be number of unique_server_ids
            query.set_query_ans(n - len(unique_server_ids))

        # sort the query_arr according to idx
        query_arr.sort(key=lambda x: x.get_query_idx())
        ans_arr = []
        for query in query_arr:
            ans_arr.append(query.get_query_ans())
        return ans_arr

