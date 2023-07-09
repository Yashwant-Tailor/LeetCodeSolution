/*
points to remember
1. keep the head otherwise you will get confuse if you only work with the ans .
2. don't forget to update l1 or l2 and then current pointer of merged list (which is ans) .
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ans = nullptr  , *head  = nullptr;
        while( l1 != nullptr || l2 != nullptr){
            if(ans == nullptr){
                if(l2 == nullptr){
                    ans  =  l1 ; 
                    l1 = l1->next ; 
                }
                else if(l1 == nullptr){
                    ans = l2 ; 
                    l2 = l2->next ; 
                }
                else if(l1->val > l2->val){
                    ans = l2 ; 
                    l2 = l2->next ; 
                }
                else{
                    ans = l1 ; 
                    l1 = l1->next ; 
                }
                head = ans ; 
            }
            else{
                if(l1 == nullptr){
                    ans->next = l2 ;
                    l2 = l2->next ; 
                }
                else if(l2 == nullptr){
                    ans->next = l1 ; 
                    l1 = l1->next ; 
                }
                else if(l1->val > l2->val){
                    ans->next = l2 ; 
                    l2 = l2->next ; 
                }
                else{
                    ans->next = l1 ; 
                    l1 = l1->next ; 
                }
                ans = ans->next ; 
            }
        }
        return head ; 
    }
};
