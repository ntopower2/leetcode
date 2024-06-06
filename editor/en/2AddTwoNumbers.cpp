// #include "iostream"
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *init1 = l1, *init2 = l2;
        int carry = 0, sum;
        while (l1 != nullptr && l2 != nullptr)
        {
            sum = l1->val + l2->val + carry;
            carry = (sum > 9);
            l1->val = sum % 10;
            l2->val = sum % 10;
            if (carry && !l1->next && !l2->next)
            {
                l1->next = new ListNode(carry);
                return init1;
            }
            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1 != nullptr)
        {
            sum = l1->val + carry;
            carry = (sum > 9);
            l1->val = sum % 10;
            if (carry && !l1->next)
            {
                l1->next = new ListNode(carry);
                return init1;
            }
            l1 = l1->next;
        }
        while (l2 != nullptr)
        {
            init1 = init2;
            sum = l2->val + carry;
            carry = (sum > 9);
            l2->val = sum % 10;
            if (carry && !l2->next)
            {
                l2->next = new ListNode(carry);
                return init2;
            }
            l2 = l2->next;
        }
        return init1;
    }
};
