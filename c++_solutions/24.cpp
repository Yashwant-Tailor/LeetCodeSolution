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
    ListNode* swapPairs(ListNode* head) {
        ListNode* currNode = head , *previous = nullptr ; 
        while(currNode != nullptr && currNode->next != nullptr){
            ListNode* nextNode = currNode->next ; 
            currNode->next = nextNode->next ; 
            nextNode->next = currNode ;
            if(previous != nullptr){
                previous->next = nextNode ; 
            }
            else{
                head = nextNode ; 
            }
            previous = currNode ;
            currNode = currNode->next ; 
        }
        return head ; 
    }
};
