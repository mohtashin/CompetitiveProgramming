#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long a, b, c, d;

    cin >> a >> b >> c >> d;

    if (a+b-c==d or a+b*c==d or a-b+c==d or a-b*c==d or a*b+c==d or a*b-c==d) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }


}



