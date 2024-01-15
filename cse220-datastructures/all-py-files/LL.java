public class LL {
    // ==============================
    // lec1

    Node head = null;

    public LL(int[] arr) {

        if (arr.length == 0) {
            System.out.println("Arry is empty");
            return;
        }

        Node tail = null;
        for (int i = 0; i < arr.length; i++) {
            if (head == null) {
                head = new Node(arr[i], null);
                tail = head;
            } else {
                tail.next = new Node(arr[i], null);
                tail = tail.next;
            }
        }
    }

    /*
     * @beginning
     * 
     * @middle
     * 
     * @end How the fucke you insert into
     */

    public void insertAt(int size, int index, int item) {
        // will this method & all condition works for insert ende??
        // how this works?
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
        tmp.next = new_node;
        // tmp = new_node; // here was the error

        /* How the fuckint! a am directly able to call nodeat */
        /* Why we need pred ?? */
        // Node pred = nodeAt(index - 1);
        // new_node.next = pred.next;
        // pred.next = new_node;
    }

    public Node nodeAt(int at) {
        Node current_node = this.head;
        for (int i = 0; i < at; i++) {
            current_node = current_node.next;
            if (current_node == null) {
                System.out.println("Node is empty! can't return node!");
                return null;
            }
        }
        return current_node;
    }

    public void remove(int size, int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }

        Node removedNode = null;
        if (index == 0) {
            removedNode = head;
            head = head.next;
        } else {
            /* Why we need pred ?? */
            Node pred = nodeAt(index - 1);
            removedNode = pred.next;
            pred.next = removedNode.next;
        }

        // wtf!
        removedNode.next = null;
        removedNode = null;
        // removedNode.data = null; // error

    }

    public void print() {
        if (this.head == null) {
            System.out.println("Nothing to print!!");
            return;
        }

        Node tmp = this.head;
        while (tmp.next != null) {
            System.out.print(tmp.data + "-> ");
            tmp = tmp.next;
        }
        if (tmp != null) {
            System.out.println(tmp.data);
            ;
        }
    }
    // ==============================
    // lec2

    // ==============================
    // lec3

}
