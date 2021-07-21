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
    ListNode* reverseList(ListNode* head) {
        ListNode * tail  = NULL  , * currNode = head ; 
        while(currNode != NULL){
            ListNode * node = currNode ; 
            currNode = currNode->next ; 
            node->next = NULL;
            if(tail == NULL){
                head = node ; 
                tail = head ; 
            }
            else{
                node->next = tail ; 
                tail = node ; 
            }
        }
        return tail ; 
    }
};
