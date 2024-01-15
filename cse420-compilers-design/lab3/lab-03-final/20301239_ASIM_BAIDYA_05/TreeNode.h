#ifndef TREE_NODE_H
#define TREE_NODE_H

#include <iostream>
#include <string>
#include <vector>

extern int indentation_offset;
extern bool need_indentation;

class TreeNode {
   private:
    std::string type;
    std::string value;
    std::vector<TreeNode*> children;
    int pad;

   public:
    TreeNode(const std::string& type, const std::string& value = "",
             int pad = 0)
        : type(type), value(value), pad(pad) {
    }

    static TreeNode* createNonTerminalNode(const std::string& type) {
        TreeNode* node = new TreeNode(type);
        return node;
    }

    static TreeNode* createTerminalNode(const std::string& type,
                                        const std::string& value = "",
                                        int pad = 0) {
        TreeNode* node = new TreeNode(type, value);
        node->pad = pad;
        return node;
    }

    void addChild(TreeNode* child) {
        children.push_back(child);
    }

    const std::string& getType() const {
        return type;
    }

    const std::string& getValue() const {
        return value;
    }

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

    const std::vector<TreeNode*>& getChildren() const {
        return children;
    }

    int getNumChildren() const {
        return children.size();
    }

    void postOrderTraversal(std::ofstream& outFile) {
        for (auto child : children) {
            child->postOrderTraversal(outFile);
        }

        if (!value.empty()) {
            outFile << getFormattedValue();
        }
    }

    ~TreeNode() {
        for (auto child : children) {
            delete child;
        }
    }
};

#endif  // TREE_NODE_H
