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
        ListNode * curr = head  , * previous = nullptr; 
        head = nullptr ; 
        while(curr != nullptr){
            int uniqueVal = curr->val ;
            ListNode* uniqueNode = curr ;
            int countVal = 0 ; 
            while(curr != nullptr && curr->val == uniqueVal){
                curr = curr->next ; 
                countVal++  ;
            }
            uniqueNode->next = nullptr ;
            if(countVal == 1){
                if(previous == nullptr){
                    head = uniqueNode ; 
                    previous = head ;
                }
                else{ 
                    previous->next = uniqueNode ; 
                    previous = previous->next ; 
                }
            }
        }
        return head ; 
    }
};
