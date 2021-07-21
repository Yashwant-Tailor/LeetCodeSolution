/*
reverse the list from the half and then compare the element as we compare for palindrome
just remember the syntax cause tried to intialize the pre at NULL don't try to point node each other 
cause I got error and don't know the exact reason for the error . 
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
    bool isPalindrome(ListNode* head) {
        int length = 0 ; 
        ListNode* curr = head ; 
        while(curr != NULL){
            length++ ; 
            curr = curr->next ; 
        }
        int halfL  = length/2 ; 
        curr  = head ; 
        ListNode * pre = NULL ; 
        while(halfL--){
            pre = curr ; 
            curr = curr->next ; 
        }
        pre = NULL ; 
        while(curr != NULL){
            ListNode* tail = curr; curr = curr->next ; 
            tail->next = pre ; 
            pre = tail ;
        }
        bool ans = true ; 
        halfL = length/2 ; 
        ListNode * left = head , *right = pre ; 
        while(halfL--){
            ans &= (left->val == right->val) ; 
            left = left->next ; 
            right = right->next ; 
        }
        return ans ; 
    }
};
