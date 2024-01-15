public class Main {
    public static void main(String[] args) {

        int[] arr = { 1, 2, 3, 4, 5 };
        // LL ll = new LL(arr);

        // ll.insertAt(5, 2, 383);
        // ll.insertAt(6, 3, 399);
        // ll.insertAt(7, 7, 993);
        // ll.print();

        // ll.remove(7, 6);
        // ll.remove(6, 0);
        // ll.remove(5, 0);
        // ll.remove(4, 0);
        // ll.print();

        // ==============================
        // lec2
        Node head = createList(arr);
        print(head);

        Node head_copy = copyList(head);
        print(head_copy);

        // ==============================
        // lec3

    }

    // ==============================
    // lec2

    public static Node createList(int[] array) {
        Node head = null;
        Node tail = null;

        for (int i = 0; i < array.length; i++) {
            Node new_node = new Node(array[i], null);
            if (head == null) {
                head = new_node;
                tail = new_node;
            } else {
                tail.next = new_node;
                tail = new_node;
            }

        }

        return head;

    }

    public static void print(Node head) {
        if (head == null) {
            System.out.println("Nothing to print!!");
            return;
        }

        Node tmp = head;
        while (tmp.next != null) {
            System.out.print(tmp.data + "-> ");
            tmp = tmp.next;
        }
        if (tmp != null) {
            System.out.println(tmp.data);
            ;
        }
    }

    public static Node copyNode(Node n) {
        return new Node(n.data, null);
    }

    public static Node copyList(Node head) {
        Node new_head = null;
        Node new_tail = null;
        Node current_node = head;
        while (current_node != null) {
            Node copy = copyNode(current_node);
            current_node = current_node.next;
            if (new_tail == null) {
                new_head = copy;
                new_tail = copy;
            } else {
                new_tail.next = copy;
                new_tail = copy;
            }

        }
        return new_head;
    }
    // ==============================
    // lec3

}