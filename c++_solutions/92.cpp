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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode * tail1 = nullptr , * head1 = nullptr , * start = nullptr , *end = nullptr , *curr= head , *previous = nullptr ; 
        int index = 0 ; 
        while(curr != nullptr){
            index++  ;
            if(index == left ){
                tail1 = previous ; 
                if(tail1 != nullptr){
                    tail1->next = nullptr ; 
                }
                start = curr  ; 
                curr = curr->next ; 
                start->next = nullptr ; 
                end = start ;
                head1 = curr ;
            }
            else if(index > left && index < right){
                ListNode * node = curr ; 
                curr = curr->next ; 
                node->next = end ; 
                end = node ;
                head1 = curr ;
            }
            else if(index == right){
                ListNode * node = curr ; 
                curr = curr->next ; 
                node->next = end ; 
                end = node ; 
                head1 = curr ; 
            }
            else{
                previous = curr ;
                curr = curr->next ; 
            }
        }
        if(tail1 == nullptr){
            start->next = head1 ; 
            return end ;
        }
        else{
            cout<<"ok\n" ; 
            tail1->next = end ; 
            start->next = head1 ; 
            return head ; 
        }
    }
};
