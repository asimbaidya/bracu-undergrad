# Formatter

formatter with cfg rules


```cpp
    std::string getFormattedValue() const {
        std::string fmt_value = value;

        if (type == "LCURL") {
            indentation_offset++;
        } else if (type == "RCURL") {
            indentation_offset--;
            if (indentation_offset == 0) {
                need_indentation = true;
            }
        }

        if (need_indentation) {
            std::cout << "INSIDE FOR: " << indentation_offset << "\n\n";
            for (int i = 0; i < indentation_offset; i++) {
                fmt_value = "    " + fmt_value;
            }
            need_indentation = false;
        }

        // 1 - ' ' - after
        // 2 = '\n' - after
        // 3 = ' ' - before
        // 4 = ' ' - before and after
        if (pad == 1) {
            fmt_value = fmt_value + " ";
            std::cout << "pad is 1" << std::endl;
        } else if (pad == 2) {
            fmt_value = fmt_value + "\n";
            need_indentation = true;
            std::cout << "pad is 2 " << type << std::endl;
        } else if (pad == 3) {
            fmt_value = " " + fmt_value;
            std::cout << "pad is 3" << std::endl;
        } else if (pad == 4) {
            fmt_value = " " + fmt_value + " ";
            std::cout << "pad is 4" << std::endl;
        }

        return fmt_value;
    }
```
