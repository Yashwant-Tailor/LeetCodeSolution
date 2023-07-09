/*
best method to avoid any confusion 
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
    ListNode* partition(ListNode* head, int x) {
        ListNode *curr = head , * headGre = nullptr , *headLess = nullptr , *tailGre = nullptr , * tailLess = nullptr ; 
        while(curr != nullptr){
            ListNode * tempNode = curr ; 
            curr = curr->next ; 
            tempNode->next = nullptr ; 
            if(tempNode->val < x){
                if(headLess == nullptr){
                    headLess = tempNode ; 
                    tailLess = tempNode ; 
                }
                else{
                    tailLess->next = tempNode ; 
                    tailLess = tempNode ; 
                }
            }
            else{
                if(headGre == nullptr){
                    headGre = tempNode ; 
                    tailGre = tempNode ; 
                }
                else{
                    tailGre->next = tempNode;
                    tailGre = tempNode ;
                }
            }
        }
        if(tailLess == nullptr){
            return headGre ; 
        }
        else{
            tailLess->next = headGre ; 
            return headLess ; 
        }
    }
};
