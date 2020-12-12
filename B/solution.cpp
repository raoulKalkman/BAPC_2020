#include <iostream> // std in/out
#include <fstream> // files
#include <string> // Datatype
#include <cmath> // Standard math, constants in <numbers>
#include <numeric> // More functions, like gcd
#include <ctime> // datetime
#include <algorithm> // replace, sort, all/any
#include <vector> // Dynamic array (default)
using namespace std;


// Generate palins of specific length in range
void gen_palin(vector<int> &palins, int range[2], int len, int num[], int at=0) {
  for (int dig = 0; dig < 10; dig++) {
    num[at] = dig;
    num[len-1-at] = dig; // Symmetric

    if (at == ceil(len/2.0)-1) {
      if (!(len > 1 && num[0] == 0)) {
        int number = 0;
        for (int i = 0; i < len; i++) {
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
void gen_palin_range(vector<int> &palins, int range[2]) {
  for (int n = ceil(log10(range[0])); n <= ceil(log10(range[1])); n++) { // All possible lengths
    int num[n];
    gen_palin(palins, range, n, num);
  }
}


int main() {
  int n;
  cin >> n;

  vector<int> palins;
  int r[2] = {2, n};
  gen_palin_range(palins, r);

  for (auto a : palins) {
    int left = n - a;
    for (auto b : palins) {
      int c = left - b;
      if (c > 0 && find(palins.begin(), palins.end(), c) != palins.end()) {
        cout << 3 << endl;
        cout << a << endl;
        cout << b << endl;
        cout << c << endl;
        return 0;
      }
    }
  }

}
