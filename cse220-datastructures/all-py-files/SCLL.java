public class SCLL {
    public static void main(String[] args) {
        // circular single linked list
        for (Node n = head; n.next != head; n = n.next) {
            // hot stuff
        }

        // dummy headed circular single linked list
        for (Node n = head.next; n.next != head; n = n.next) {
            // do stuff
        }
    }

}
