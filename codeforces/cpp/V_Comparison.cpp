#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int A, B;
    char S;

    cin >> A >> S >> B;
    bool correct;
    if (S == '>') {
        correct = A>B;
    }
    else if (S == '<') {
        correct= A<B;
    }
    else if (S =='=') {
        correct= A==B;
    }
    if (correct){
        cout<< "Right";
    }
    else {
        cout<<"Wrong";
    }

}
