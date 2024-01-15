// normal insert
public class note {
    public void insertAt(int size, int index, int item) {

        // problem section
        if (index < 0 || index > size) {
            System.out.println("invalid index");
            return;
        }

        Node new_node = new Node(item, null);
        if (index == 0) {
            new_node.next = this.head;
            this.head = new_node;
            return;
        }
        Node tmp = this.head;
        for (int i = 0; i < index - 1; i++) {
            tmp = tmp.next;
        }
        new_node.next = tmp.next;
    }

    // dmmy insert
    public void insertAt(int size, int index, int item) {

        // problem section
        if (index < 0 || index > size) {
            System.out.println("invalid index");
            return;
        }

        Node new_node = new Node(item, null);
        Node tmp = this.head.next;
        for (int i = 0; i < index - 1; i++) {
            tmp = tmp.next;
        }
        new_node.next = tmp.next;
    }

    public static void main(String[] args) {

        // normal iteraton
        for (Node n = head; n != null; n = n.next) {
            // do stuff
        }

        // dummy iteration
        for (Node n = head.next; n != null; n = n.next) {
            // do stuff
        }
    }

}
