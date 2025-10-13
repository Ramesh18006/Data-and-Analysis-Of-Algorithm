#include <iostream>
#include <string>
using namespace std;

int main() {
    string text;
    string word = "the";

    cout << "Enter a sentence: ";
    getline(cin,text); // read full sentence

    cout << "\nIndices of 'the' in the string:\n";

    int n = text.length();
    int m = word.length();

    // loop through each character of text
    for (int i = 0; i <= n - m; i++) {
        bool match = true;

        // check if substring starting from i matches "the"
        for (int j = 0; j < m; j++) {
            if (text[i + j] != word[j]) {
                match = false;
                break;
            }
        }

        // if all characters match, print index
        if (match) {
            cout << i << " ";
        }
    }

    cout << endl;
    return 0;
}
