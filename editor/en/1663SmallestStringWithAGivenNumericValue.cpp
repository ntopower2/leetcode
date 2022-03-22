#include "iostream"
#include "string"

using namespace std;
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string getSmallestString(int n, int k) {
        string res;
        res.append(n,'a');
        int num;
        k-=n;
        while (k>0) {
            num = min(k, 25);
            res[--n] = 'a' + num;
            k-=num;
        }
        return res;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    auto c = Solution();
    cout << c.getSmallestString(3,27);
}
