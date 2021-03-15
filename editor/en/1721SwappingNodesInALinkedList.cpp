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
        ListNode* lst[(int)1e5];
        int n = 0;
        while (curr) {
            lst[n++] = curr;
            curr = curr->next;
        }
        if (n==2) {
            lst[0]->next= nullptr; lst[1]->next=lst[0];
            return lst[1];
        }
        first = lst[(k>n/2)?n-k:k-1]; second = lst[(k>n/2)?k-1:n-k];
        if (first!=lst[0])
            prevf = lst[(k>n/2)?n-k-1:k-2], prevf->next = second;
        if (second!=lst[0])
            prevs=lst[(k>n/2)?k-2:n-k-1], prevs->next = first;
        swap(first->next, second->next);
        return (first==lst[0])?second:lst[0];
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    auto s = new Solution();
    int arr[] = {47,62,39,94,90,17,74,83,70,12,99,29,73};
//    int arr[] = {1,2};
    int n=13, k=1;
    ListNode l[n];
    l[n-1].val = arr[n-1]; l[n-1].next = nullptr;
    for (int i=n-2;i>=0;--i) l[i].val=arr[i], l[i].next = &l[i+1];
    cout << s->swapNodes(&l[0], k)->val;
}
