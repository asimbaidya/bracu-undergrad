public class LLSTack {

    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(30);
        s.push(40);
        s.push(51);
        s.print();
        s.pop();
        System.out.println(s.peek());
    }
}

class Node {
    int data;
    Node next;

    public Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}

class Stack {
    Node head;

    public void push(int data) {
        Node newNode = new Node(data, this.head);
        this.head = newNode;
    }

    public int peek() {
        if (this.head == null) {
            System.out.println("The stack is empty!");
            // return null;
            return -1;
        } else {
            return this.head.data;
        }
    }

    public int pop() {
        if (this.head == null) {
            System.out.println("The stack is empty!");
            // return null;
            return -1;
        } else {
            Node tmp = this.head;
            this.head = tmp.next;
            return tmp.data;
        }

    }

    public void print() {
        Node tmp = this.head;
        while (tmp != null) {
            System.out.print(tmp.data + " ");
            tmp = tmp.next;
        }
        System.out.println();
    }
}
