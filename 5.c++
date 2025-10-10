#include <iostream>
#include <string>
using namespace std;
int main() {
    string pattern = "ABCBCABC";
    int n = pattern.length();
    int lps[100];   
    lps[0] = 0;     
    int len = 0;    
    int i = 1;      
    while (i < n) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1]; 
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    cout << "Pattern: " << pattern << "\n";
    cout << "Index : ";
    for (int j = 0; j < n; j++) cout << j << " ";
    cout << "\nChar  : ";
    for (int j = 0; j < n; j++) cout << pattern[j] << " ";
    cout << "\nLPS   : ";
    for (int j = 0; j < n; j++) cout << lps[j] << " ";
    cout << "\n";
    return 0;
}
