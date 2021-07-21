/*
very classical problem . 
Very high chance that in interview you will face this question .
So try to see this algorithm from every angle like .... 
time complexity 
space complexity
edge cases
on which node we will have the cycle start if we start traversing the list from the given head .
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL){
            return false ; 
        }
        ListNode * shortStep = head , *longStep = head->next ;
        while(shortStep != longStep){
            if(longStep){
                longStep = longStep->next  ;
                if(longStep){
                    longStep = longStep->next ;
                    shortStep = shortStep->next ; 
                }
                else{
                    return false ;
                }
            }
            else{
                return false ;
            }
        }
        return true ; 
    }
};
