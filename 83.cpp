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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode * curr = head ; 
        while(curr != nullptr){
            ListNode * uniqueNode = curr ; 
            curr = curr->next ; 
            while(curr != nullptr && uniqueNode->val == curr->val){
                curr = curr->next ; 
            }
            uniqueNode->next = curr ; 
        }
        return head ; 
    }
};
