#include "string"
#include "iostream"

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows==1 || s.length() < numRows)
            return s;
        const int step = 2*numRows-2;
        string res;
        string temp[numRows];
        for (int i=0; i<s.length();i++)
            if (i%step>=numRows) temp[step-(i%step)]+= s[i];
            else if (i+1==numRows) temp[numRows-1]+=s[i];
            else temp[i%step]+=s[i];
        for (const string& t:temp) res+=t;
        return res;
    }

    string display(string s, int numRows) {
        if (numRows==1 || s.length() < numRows)
            return s;
        const int step = 2*numRows-2;
        const int chunks = s.length()/step;
        const int rem = s.length()%step;
        string res, temp;
        //row 0
        for (int i=0;i<chunks;i++) {
            res+= s[i*step];
            res+= mulstr(" ", 2*numRows-3);
        }
        if (rem) res+= s[chunks*step];
        res+="\n";
        for (int row=1; row<numRows-1 && numRows>2;row++) {
            for (int i=0;i<chunks;i++) {
                temp = s[i*step+row];
                temp += mulstr(" ", 2*numRows-3);
                temp[2*(numRows-row-1)] = s[step-row+i*step];
                res+= temp;
            }
            if (rem>row) res+=s[chunks*step + row];
            res+="\n";
        }
        //row last
        for (int i=0;i<chunks;i++) {
            res+= s[numRows-1+i*step];
            res+= mulstr(" ", 2*numRows-3);
        }
        if (rem>=numRows && numRows>2) res+= s[numRows-1+chunks*step];
        res+="\n";
        return res;
    }

    string mulstr(string s, int num) {
        string res;
        for (int i=0;i<num;i++) res+=s;
        return res;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    Solution s;
    cout << s.convert("PAYPALISHIRING", 3);
}