#include <iostream> // std in/out
#include <cmath> // Standard math, constants in <numbers>
#include <algorithm> // replace, sort, all/any
#include <vector> // Dynamic array (default)
using namespace std;


// Generate palins of specific length in range
void gen_palin(vector<long int> &palins, long int range[2], long int len, long int num[], long int at=0) {
  for (long int dig = 0; dig < 10; dig++) {
    num[at] = dig;
    num[len-1-at] = dig; // Symmetric

    if (at == ceil(len/2.0)-1) {
      if (!(len > 1 && num[0] == 0)) {
        long int number = 0;
        for (long int i = 0; i < len; i++) {
          number += num[i] * pow(10, len-1-i);
        }
        if (number >= range[0] && number <= range[1]) {
          palins.push_back(number);
        }
      }
    } else {
      gen_palin(palins, range, len, num, at+1); // Recurse
    }
  }
}

// Generate palindromic numbers between range
void gen_palin_range(vector<long int> &palins, long int range[2]) {
  for (long int n = ceil(log10(range[0])); n <= ceil(log10(range[1])); n++) { // All possible lengths
    long int num[n];
    gen_palin(palins, range, n, num);
  }
}


int main() {
  long int n;
  cin >> n;

  vector<long int> palins;
  long int r[2] = {2, n};
  gen_palin_range(palins, r);
  sort(palins.begin(), palins.end());

  for (auto a : palins) {
    long int left = n - a;
    for (auto b : palins) {
      long int c = left - b;
      if (c > 0 and binary_search(palins.begin(), palins.end(), c)) {
        cout << 3 << endl;
        cout << a << endl;
        cout << b << endl;
        cout << c << endl;
        return 0;
      }
    }
  }


 return 0;
}
