#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int A, B;

    cin >> A >> B;
    if (A%B==0 or B%A==0){
        cout<< "Multiples";
    }
    else {
        cout<< "No Multiples";
    }
}
