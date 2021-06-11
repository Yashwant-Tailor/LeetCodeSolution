// sorting  , greedy (a[i] + a[j] + a[k] == 0 := -a[i] = a[j] + a[k]) 
// two pointer for (a[j] + a[k])
// for unique pair we have consider the count of a  element 
// case 1 : when we take an element only once in triplet 
// case 2: when we take an elment twice in triplet
// corner case when a[i] = 0 and count of 0 is more than 2
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& A) {
        
        vector<vector<int>>ans ; 
        int n = A.size() ; 
        sort(A.begin() , A.end()) ; 
        vector<int>a , b ; 
        int i1 = 0 ; 
        while(i1 < n){
            int temp = A[i1]  ,count = 0 ; 
            while(i1 < n && temp == A[i1]){
                i1++ ; count++  ;
            }
            a.push_back(temp) ; 
            b.push_back(count) ; 
        }
        for(int  i = 0 ; i  < a.size() ; i++){
            int j = i+1  , k = a.size() -1 ; 
            while(j < k){
                if(a[i] + a[j] + a[k] == 0){
                    vector<int>temp ; 
                    temp.push_back(a[i]) ; temp.push_back(a[j]) ; temp.push_back(a[k]) ; 
                    ans.push_back(temp) ; 
                }
                if(a[i] + a[j] + a[k] <= 0){
                    j++ ; 
                }
                else{
                    k--; 
                }
            }
            if(j < a.size() && b[j] >= 2 && 2*a[j] + a[i] == 0){
                vector<int>temp ; 
                temp.push_back(a[i]) ; 
                temp.push_back(a[j]) ; 
                temp.push_back(a[j]) ; 
                ans.push_back(temp) ; 
            }
            if(b[i] > 1){
                j = i+1  ; k  = a.size() ;  
                while(j < k){ 
                    if(2*a[i] + a[j] == 0){
                        vector<int>temp ; 
                        temp.push_back(a[i]) ; 
                        temp.push_back(a[i]) ; 
                        temp.push_back(a[j]) ; 
                        ans.push_back(temp) ; 
                    }
                    j++ ; 
                }
            }
            if(b[i] > 2 && a[i] == 0){
                vector<int>temp ; 
                temp.push_back(0) ; temp.push_back(0) ; 
                temp.push_back(0) ; 
                ans.push_back(temp) ;
            }
        }
        return ans ; 
    }
};