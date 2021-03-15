//leetcode submit region begin(Prohibit modification and deletion)
#include "iostream"
#include "vector"
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        if (!head->next) return head;
        ListNode* curr = head, *first, *second, *prevf, *prevs;
        int n = 0, i=1;
        if (k==1) prevf = nullptr, first = head;
        while (curr) {
            if (++i==k && k!=1)
                prevf = curr, first = curr->next;
            n++;
            curr = curr->next;
        }
        if (n==2) {
            curr = head->next;
            curr->next = head;
            head->next = nullptr;
            return curr;
        }
        if (k>=n/2) {
            i=1;
            prevs = prevf;
            second = first;
            prevf = head; first=prevf->next;
            if (k==n)
                prevf = nullptr, first = head;
            while (i++<n-k && k!=n-1) {
                prevf=prevf->next;
                first=prevf->next;
            }
        } else {
            i=0;
            prevs = first;
            while (i++<n-2*k) {
                prevs=prevs->next;
                second=prevs->next;
            }
        }
        if(prevf) prevf->next = second;
        if (first->next==second) {
            first->next = second->next;
            second->next=first;
        } else {
            swap(second->next,first->next);
            prevs->next = first;
        }
        if (head==first) return second;
        else return head;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    auto s = new Solution();
    int arr[] = {55,60,78,53,93,37,31,4,61,11,13,51,34,83,24,96,5,77,1,67};
//    int arr[] = {1,2};
    int n=20, k=11;
    ListNode l[n];
    l[n-1].val = arr[n-1]; l[n-1].next = nullptr;
    for (int i=n-2;i>=0;--i) l[i].val=arr[i], l[i].next = &l[i+1];
    cout << s->swapNodes(&l[0], k)->val;
}
