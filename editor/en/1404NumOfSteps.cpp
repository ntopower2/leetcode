#include "bitset"
#include "string"
#include "iostream"

class Solution
{
public:
    int numSteps(std::string s)
    {
        int p = s.length();
        std::bitset<s.length()> bits{s};
        int t = 0;
    }
};

int main()
{
    Solution s;
    std::cout << s.numSteps("1");
}