class Solution:
    def get_report_type(self,report,p_feedback,n_feedback):
        words = report.split(' ')
        points = 0
        for word in words:
            if word in p_feedback:
                points += 3
            elif word in n_feedback:
                points -= 1
        return points
    
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # Solution Overview
        # for positive and negative feedback create hashmap (it will help us to find the report[i] is having positive or negative feedback)
        # for each reporst we will mark it as positive or negative
        # after that we can calculate the score of each student
        # now we can use heap to find the top k student
        p_feedback = set()
        n_feedback = set()
        for feedback in positive_feedback:
            p_feedback.add(feedback)
        for feedback in negative_feedback:
            n_feedback.add(feedback)
        for i in range(len(report)):
            report[i] = self.get_report_type(report[i],p_feedback,n_feedback)
        import heapq as hp
        min_heap = []
        class NODE:
            def __init__(self,points,s_id):
                self.s_id = s_id
                self.points = points
            def __lt__(self,other):
                if other.points == self.points:
                    return self.s_id > other.s_id
                return self.points < other.points
        for idx,points in enumerate(report):
            s_id = student_id[idx]
            if len(min_heap) < k:
                hp.heappush(min_heap,NODE(points,s_id))
            elif min_heap[0].points < points or (min_heap[0].points == points and min_heap[0].s_id > s_id):
                hp.heappop(min_heap)
                hp.heappush(min_heap,NODE(points,s_id))
        ans = []
        while len(min_heap) > 0:
            ans.append(min_heap[0].s_id)
            hp.heappop(min_heap)
        return ans[::-1]


