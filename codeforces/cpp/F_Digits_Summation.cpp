#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string N, M;
    cin >> N >> M;
    int sum = (N[N.size()-1] - '0') + (M[M.size()-1] - '0');
    cout << sum;
}
