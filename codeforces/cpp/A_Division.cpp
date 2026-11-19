#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    int temp;

    for (int i=0; i<t; i++){
        cin >> temp;

        if (temp <=1399){

            cout<< "Division 4 \n";
        }
        else if (1400 <= temp && temp<=1599) {
            cout<< "Division 3 \n";
        }
        else if (1600 <= temp && temp<=1899) {
            cout<< "Division 2 \n";
        }
        else {
            cout<< "Division 1 \n";
        }
    }
}
