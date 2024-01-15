public class BinaryTree {
  public static void main(String[] args) {
    Node root = new Node(10, null, null, null);

    Node n2 = new Node(5, null, null, null);
    Node n3 = new Node(7, null, null, null);
    Node n4 = new Node(17, null, null, null);
    Node n5 = new Node(9, null, null, null);
    Node n6 = new Node(28, null, null, null);

    // childs of root
    root.left = n2;
    n2.parent = root;

    root.right = n3;
    n3.parent = root;

    // childs of node 2
    n2.left = n4;
    n4.parent = n2;

    n2.right = n5;
    n5.parent = n2;

    // childs of node 3
    n3.right = n6;
    n6.parent = n3;

    // arr representation
    int[] arr = {0, 10, 5, 7, 17, 9, 0, 28};

    Node root_two = createTree(arr, 1);

    // test heightu
    //
    System.out.println("Height of tree: " + height_of_tree(root_two));

    // test level
    System.out.println("Level of tree:" + level(root_two));
    System.out.println("Level of tree:" + level(n4));
    System.out.println("Level of tree:" + level(n2));

    // test pre-order
    // pre_order(root_two);
    pre_order(root);
  }

  public static Node createTree(int[] a, int i) {

    if (i < 0 || i >= a.length || a[i] == 0) {
      return null;
    }
    Node root = new Node(a[i], null, null, null);
    root.left = createTree(a, 2 * i);
    root.right = createTree(a, 2 * i + 1);

    if (root.left != null) {
      root.left.parent = root;
    }
    if (root.right != null) {
      root.right.parent = root;
    }

    return root;
  }

  // task height of binary tree
  public static int height_of_tree(Node root) {
    if (root == null) {
      return 0;
      // calculate wrong if return -1;
    }
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right));
  }
  public static int max(int l, int r) {
    if (l > r)
      return l;
    return r;
  }

  // task level of a binary tree
  public static int level(Node node) {
    if (node.parent == null)
      return 0;
    return 1 + level(node.parent);
  }

  // pre-order
  public static void pre_order(Node root) {
    if (root == null)
      return;
    System.out.println(root.elem);
    pre_order(root.left);
    pre_order(root.right);
  }
  // in-order
  public static void in_order(Node root) {
    if (root == null)
      return;
    pre_order(root.left);
    System.out.println(root.elem);
    pre_order(root.right);
  }
  // post order
  public static void post_order(Node root) {
    if (root == null)
      return;
    pre_order(root.left);
    pre_order(root.right);
    System.out.println(root.elem);
  }
  //
}
