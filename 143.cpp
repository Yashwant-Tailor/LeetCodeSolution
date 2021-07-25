/*
simple list algo 
first find the mid to right end part 
reverse it 
then merge left to mid with mid+1 to right
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
    void reorderList(ListNode* head) {
        ListNode * curr = head  ; 
        int len = 0 ; 
        while(curr != NULL){
            len++ ; curr = curr->next ; 
        }
        int hf  = (len+1)/2 ; 
        curr = head ; 
        ListNode * pre = NULL ; 
        while(hf--){
            pre = curr ; 
            curr = curr->next ;
        }
        if(pre != NULL)pre->next = NULL ; 
        ListNode * head1 = head , *head2 = curr ; 
        curr = head2 ; 
        head2 = NULL ; 
        while(curr != NULL){
            ListNode * node = curr; curr = curr->next ; node->next = NULL ;
            if(head2 == NULL){
                head2 = node ; 
            }
            else{
                node->next = head2 ; 
                head2 = node ; 
            }
        }
        head = NULL ; pre = NULL  ; 
        while(head1 != NULL && head2 != NULL){
            ListNode * node1 = head1 ; head1 = head1->next ; 
            ListNode* node2 = head2 ; head2 = head2->next ; 
            node1->next = NULL ; 
            node2->next = NULL ;
            if(head==NULL){
                head = node1 ; 
                node1->next = node2 ; 
                pre  = node2 ; 
            }
            else{
                node1->next = node2 ; 
                pre->next = node1 ; 
                pre = node2 ; 
            }
        }
        if(head1){
            head1->next = NULL ;
            if(pre){
                pre->next = head1 ;
            }
            else{
                head  = head1 ;
            }
        }
        return ; 
    }
};
