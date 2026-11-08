#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int k, n, w;
  cin >> k >> n >> w;
  int sum;
  sum = 0;
  for (int i = 1; i < w+1; i++) {
    sum += k * i;
  }
  int remainder;
  remainder = sum - n;

  if (remainder <= 0) {
    cout << 0;
  } else {
    cout << remainder;
  }
}




