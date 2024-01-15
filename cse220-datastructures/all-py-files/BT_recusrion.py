# Tree implementation using nodes
class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree:
    def __init__(self, array):
        self.root = Node(array[0])
        pass


# ----------------------------------------


# task 1
def height(tree):
    pass
    #


# task 1


def level(tree, node):
    pass


# task 3


def pre_order(node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


# task 4
def in_order(node):
    if node is None:
        return
    pre_order(node.left)
    print(node.data)
    pre_order(node.right)


# task 5
def post_order(node):
    if node is None:
        return
    pre_order(node.left)
    pre_order(node.right)
    print(node.data)


# task 6.
def is_same_tree(tree_one, tree_two):
    if tree_one == None and tree_two == None:
        return True
    # if None in (tree_one, tree_two) and tree_one is not tree_two:
    # if None in (tree_one, tree_two) and tree_one is tree_two:
    if tree_one == None and tree_two != None or tree_one != None and tree_two == None:
        return False
    if tree_one.data != tree_two.data:
        return False
    return is_same_tree(tree_one.left, tree_two.left) and is_same_tree(
        tree_one.right, tree_two.right
    )


# task 7
def copy_tree(node, parent=None):
    if node == None:
        return None

    new_node = Node(node.data)

    left_child = copy_tree(node.left, new_node)
    new_node.left = left_child

    right_child = copy_tree(node.right, new_node)
    new_node.right = right_child

    new_node.parent = parent

    return new_node


# task 8 done


def get_seven_node_tree(array):
    a, b, c, d, e, f, g = array
    pati = Node(a)

    # pati.left
    pati.left = Node(b)

    # pati.right
    pati.right = Node(c)

    # pati.left.{left,right}
    pati.left.left = Node(d)
    pati.left.right = Node(e)

    # pati.right.{left,right}
    pati.right.left = Node(f)
    pati.right.right = Node(g)
    return pati


if __name__ == "__main__":
    pati = get_seven_node_tree([x for x in range(1, 8)])
    pati_two = get_seven_node_tree([x for x in range(1, 8)])
    leti = get_seven_node_tree([x for x in range(7)])

    # test
    print("PreOrder", "-" * 30)
    pre_order(pati)
    print("InOrder", "-" * 30)
    in_order(pati)
    print("Post", "-" * 30)
    post_order(pati)

    #
    print(is_same_tree(pati, leti))
    print(is_same_tree(pati, pati_two))
