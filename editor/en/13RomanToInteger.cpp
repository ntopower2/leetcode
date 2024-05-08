#include "iostream"
#include "string"

using namespace std;
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int romanToInt(string s) {
        int res=0;
        for (char c:s) {
            switch (c) {
               case 'M':
                    res+=1000;
                    break;
                case 'D':
                    res+=500;
                    break;
                case 'C':
                    res+=100;
                    break;
                case 'L':
                    res+=50;
                    break;
                case 'X':
                    res+=10;
                    break;
                case 'V':
                    res+=5;
                    break;
                case 'I':
                    res+=1;
                    break;
            }
        }
        return res;
    }
};
//leetcode submit region end(Prohibit modification and deletion)
int main() {
    auto c = Solution();
    cout << c.romanToInt("IIIU");
}