#include <bits/stdc++.h>
using namespace std;

class symbol_info {
   private:
    string sym_name;
    string sym_type;

   public:
    symbol_info(string name, string type) {
        sym_name = name;
        sym_type = type;
    }

    string getname() {
        string str = sym_name;

        size_t start = 0;
        while (start < str.length() && static_cast<char>(str[start]) == ' ') {
            start++;
        }

        size_t end = str.length();
        while (end > start && static_cast<char>(str[end - 1]) == ' ') {
            end--;
        }

        //
        sym_name = str.substr(start, end - start);
        return sym_name + " ";
    }
};
