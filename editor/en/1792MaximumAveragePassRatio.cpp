//leetcode submit region begin(Prohibit modification and deletion)
#include <algorithm>
#include "vector"
#include "iostream"
using namespace std;

#define STUD_ADD(v) (v[0]+1.0)/(v[1]+1)
#define STUD_CMP(v) STUD_ADD(v) - (v[0]*1.0/v[1])
struct heap_cmp {
    bool operator()(const vector<int>& v1, const vector<int>& v2) const{
        return STUD_CMP(v1) < STUD_CMP(v2);
    }
};

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        double res=0.0;
        make_heap(classes.begin(), classes.end(), heap_cmp());
        while (extraStudents) {
            auto p = classes.front();
            pop_heap(classes.begin(), classes.end(), heap_cmp()); classes.pop_back();
            p={p[0]+1, p[1]+1}; extraStudents--;
            classes.push_back(p); push_heap(classes.begin(), classes.end(),heap_cmp());
        }
        for (auto v:classes)
            res+=v[0]*1.0/v[1];
        res/=classes.size();
        return res;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    vector<vector<int>> classes = {{2,4},{3,9},{4,5},{2,10}};
    int extra = 4;
    auto s = new Solution();
    cout << s->maxAverageRatio(classes, extra);
}