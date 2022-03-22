#include "iostream"
#include "string"

using namespace std;
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string getSmallestString(int n, int k) {
        string res = "";
        for (int i=0;i<n && k>0;++i) {
            int num = min(k, 'z'-'a');
            char val = 'a' + num;
            res.append(&val);
            k -= num;
        }
        return res;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    auto c = Solution();
    cout << c.getSmallestString(3,27);
}
