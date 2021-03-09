#include "string"
#include "iostream"
#include "vector"

using namespace std;
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string intToRoman(int num) {
        string res;
        string num_str = to_string(num);
        for (int i=0;i<num_str.size();i++) {
            int d = num_str[i]-'0';
            switch (num_str.size()-i) {
                case 4:
                    for (int j = 0; j < num_str[i]-'0'; j++)
                        res += 'M';
                    break;
                case 3:
                    if (d==4) res+="CD";
                    else if (d==9) res+="CM";
                    else {
                        if (d>4) res+='D',d-=5;
                        for (int j = 0; j < d; j++) res += 'C';
                    }
                    break;
                case 2:
                    if (d==4) res+="XL";
                    else if (d==9) res+="XC";
                    else {
                        if (d>4) res+='L',d-=5;
                        for (int j = 0; j < d; j++) res += 'X';
                    }
                    break;
                case 1:
                    if (d==4) res+="IV";
                    else if (d==9) res+="IX";
                    else {
                        if (d>4) res+='V',d-=5;
                        for (int j = 0; j < d; j++) res += 'I';
                    }
                    break;
            }
        }
        return res;
    };
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    auto sol = new Solution();
    cout << sol->intToRoman(1994);
}