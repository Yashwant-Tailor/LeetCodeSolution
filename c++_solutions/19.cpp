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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len = 0 ; 
        ListNode* curr = head ; 
        while(curr != nullptr){
            len++ ; 
            curr = curr->next ; 
        }
        curr = head ; 
        ListNode *previous = nullptr ; 
        if( n == len){
            return head->next ; 
        }
        while(curr != nullptr){
            if(n == len){
                previous->next = curr->next ; 
                break ;
            }
            previous = curr ; 
            curr = curr->next ; 
            len-- ; 
        }
        return head ;
    }
};
