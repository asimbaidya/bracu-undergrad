public class DNode {

    int element;
    DNode next;
    DNode prev;

    public DNode(int ele, DNode next, DNode prev) {
        this.element = ele;
        this.next = next;
        this.prev = prev;
    }

    public DNode(DNode ele, DNode next, DNode prev) {
        this.next = next;
        this.prev = prev;
    }
}
