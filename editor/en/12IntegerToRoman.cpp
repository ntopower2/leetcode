#include "string"
#include "iostream"
#include "vector"
#include "map"
using namespace std;
//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string intToRoman(int num) {
        string res;
        vector<pair<int, char>> nums = {
                {1000, 'M'},
                {500,  'D'},
                {100,  'C'},
                {50,   'L'},
                {10,   'X'},
                {5,    'V'},
                {1,    'I'}
        };
        map<int, string> hundreds = {
                {0, ""},
                {1,"C"},
                {2,"CC"},
                {3,"CCC"},
                {4,"CD"},
                {5,"D"},
                {6,"DC"},
                {7,"DCC"},
                {8,"DCCC"},
                {9,"CM"}
        };
        map<int, string> tens = {
                {0, ""},
                {1,"X"},
                {2,"XX"},
                {3,"XXX"},
                {4,"XL"},
                {5,"L"},
                {6,"LX"},
                {7,"LXX"},
                {8,"LXXX"},
                {9,"XC"}
        };
        map<int, string> ones = {
                {0, ""},
                {1,"I"},
                {2,"II"},
                {3,"III"},
                {4,"IV"},
                {5,"V"},
                {6,"VI"},
                {7,"VII"},
                {8,"VIII"},
                {9,"IX"}
        };
        string num_str = to_string(num);
        for (int i=0;i<num_str.size();i++) {
            switch (num_str.size()-i) {
                case 4:
                    for (int j = 0; j < num_str[i]-'0'; j++)
                        res += 'M';
                    break;
                case 3:
                    res += hundreds[num_str[i]-'0'];
                    break;
                case 2:
                    res += tens[num_str[i]-'0'];
                    break;
                case 1:
                    res += ones[num_str[i]-'0'];
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