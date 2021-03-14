//leetcode submit region begin(Prohibit modification and deletion)
#include <algorithm>
#include "vector"
#include "iostream"
using namespace std;

#define STUD_ADD(v) (v.first+1.0)/(v.second+1)
#define STUD_CMP(v) STUD_ADD(v) - (v.first*1.0/v.second)
struct heap_cmp {
    bool operator()(pair<int, int> v1, pair<int, int> v2) const{
        return STUD_CMP(v1) < STUD_CMP(v2);
    }
};

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        double res=0.0; const int n = classes.size();
        vector<pair<int,int>> vec(n);
        for (int i=0;i<n;i++) {
            vec[i]=make_pair(classes[i][0], classes[i][1]);
        }
        make_heap(vec.begin(), vec.end(), heap_cmp());
        while (extraStudents) {
            auto p = vec.front();
            pop_heap(vec.begin(), vec.end(), heap_cmp()); vec.pop_back();
            p=make_pair(p.first+1, p.second+1); extraStudents--;
            vec.push_back(p); push_heap(vec.begin(), vec.end(),heap_cmp());
        }
        for (auto v:vec)
            res+=v.first*1.0/v.second;
        res/=n;
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