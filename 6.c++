#include <iostream>
#include <string>
using namespace std;

void computeLPS(const string &pat, int lps[]) {
    int m = pat.length();
    lps[0] = 0;
    int len = 0;  
    int i = 1;
    while (i < m) {
        if (pat[i] == pat[len]) {
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
}
void KMPSearch(const string &text, const string &pat) {
    int n = text.length();
    int m = pat.length();
    if (m == 0) {
        cout << "Empty pattern — matches at every index 0.." << n << endl;
        return;
    }
    int lps[100]; 
    computeLPS(pat, lps);
    cout << "Pattern: " << pat << "\nLPS   : ";
    for (int k = 0; k < m; ++k) cout << lps[k] << " ";
    cout << "\n\nSearching in text: " << text << "\n";
    int i = 0; 
    int j = 0; 
    bool foundAny = false;
    while (i < n) {
        if (text[i] == pat[j]) {
            i++;
            j++;
            if (j == m) {
                int startIndex = i - j;
                cout << "Pattern found at index: " << startIndex << endl;
                foundAny = true;
                j = lps[j - 1];
            }
        } else {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    if (!foundAny) cout << "Pattern not found in the text.\n";
}
int main() {
    string text  = "CATSABCBCABCDOGSABCBCABC";
    string pattern = "ABCBCABC";
    KMPSearch(text, pattern);
    return 0;
}
