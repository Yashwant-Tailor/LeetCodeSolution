class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        auto cmp = [] (long a,long b)->bool{
            return a>b ;
        };
        priority_queue<long,vector<long>,decltype(cmp)> pq(nums.begin() ,nums.end(),cmp) ; 
        int op_cnt = 0 ;
        while(pq.size() > 1 && pq.top() < k){
            long x , y ;
            x = pq.top() ; pq.pop() ;
            y = pq.top() ; pq.pop() ;
            pq.push(min(x,y) * 2 + max(x,y));
            op_cnt++;
        }
        return op_cnt ;
    }
};
