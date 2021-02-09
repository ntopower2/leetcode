class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> d;
        for (char & i : s) {
            if (i=='{' || i=='(' || i=='[') d.push(i);
            else if (d.empty()||(d.top()=='{' && i!='}')||
            (d.top()=='(' && i!=')') ||(d.top()=='[' && i!=']'))
                return false;
            else d.pop();
        }
        return d.empty();
    }
};
