#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int A, B, C;

    cin >> A >> B >> C;

    auto [low, high] =minmax({A, B, C});
    cout << low << " " << high;
}
