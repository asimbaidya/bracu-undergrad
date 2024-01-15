public class DLL {
    public static void main(String[] args) {
        // forward
        for (DNode n = head; n != null; n = n.next) {
            // cool stuff
        }

        // backward
        for (Node n = tail; n != null; n = n.prev) {
            // cool stuff
        }

        // dummy headed linked list==================
        // forward
        for (DNode n = head.next; n != null; n = n.next) {
            // cool stuff
        }

        // backward (n.prev != null)
        for (Node n = tail; n.prev != null; n = n.prev) {
            // cool stuff
        }
        // double circular linked list=============
        // forward
        for (DNode n = head; n.next != head; n = n.next) {
            // cool stuff
        }

        // backward (Node n = head.prev; n.prev != head)
        for (DNode n = head.prev; n.prev != head; n = n.prev) {
            // cool stuff
        }

        // fucking limit crossing
        // dummy headed circular linked list
        for (DNode n = head.next; n != head; n = n.next) {
            // do cool stuff
        }

        // backward
        for (DNode n = head.prev; n.prev != head; n = n.prev) {
            // do cool stuff
        }
    }
}