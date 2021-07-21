/*
conver the corner case , if you're failing in this type of list question that means you haven't convered all conrner case 
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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr){
            return head ; 
        }
        int len = 0 ; 
        ListNode* curr = head ; 
        while(curr != nullptr){
            len++  ;
            curr = curr->next ; 
        }
        k %= len ; 
        if(k == 0){
            return head ; 
        }
        curr = head ; 
        ListNode* previous = nullptr ; 
        while(len != k){
            previous = curr ; 
            curr = curr->next ; 
            len-- ; 
        }
        ListNode* headrotation = curr ; 
        if(previous != nullptr){
            previous->next = nullptr ;
        }
        while(curr != nullptr){
            previous = curr ; 
            curr = curr->next ; 
        }
        ListNode* tailrotation = previous  ; 
        tailrotation->next = head ; 
        head = headrotation ;
        return head ; 
    }
};
