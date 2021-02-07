#include <cmath>
class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        if (x<10) return true;
        int pos=0, size = floor(log10(x))+1;
        int denom = pow(10,size-1-pos);
        bool flag = true;
        while (flag && pos <= floor(size/2)-1) {
            int first = floor(x/denom), last = x%10;
            flag=(last == first);
            x%=denom;
            x/=10;
            denom/=100;
            pos++;
        }
        return flag;
    }
};
