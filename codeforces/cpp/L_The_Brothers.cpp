#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string F1, S1;
    string F2, S2;
    cin>> F1 >> S1;
    cin>> F2 >> S2;

    if (S1 == S2){
        cout << "ARE Brothers";
    }
    else {
        cout << "NOT";
    }
}
