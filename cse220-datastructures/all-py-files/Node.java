public class Node {
  int elem;
  Node left;
  Node right;
  Node parent;
  public Node(int e, Node l, Node r, Node p) {
    this.elem = e;
    this.left = l;
    this.right = r;
    this.parent = p;
  }
}
