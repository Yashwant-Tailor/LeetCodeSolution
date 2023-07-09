/*
remeber this technique 
don't update pointer intead of pointer swap the value of two adjacent pointer and then discard the 
last pointer 
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
    void deleteNode(ListNode* node) {
        ListNode * curr = node  , * nextNode = curr->next , *nexttonext = curr->next->next; 
        while(nexttonext != NULL){
            curr->val = nextNode->val ; 
            curr = nextNode ; 
            nextNode = nextNode->next ; 
            nexttonext = nexttonext->next ; 
        }
        curr->val = nextNode->val ; 
        curr->next = NULL ;
    }
};
