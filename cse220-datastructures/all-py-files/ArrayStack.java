public class ArrayStack {

    public static void main(String[] args) {
        ArrayStack s = new ArrayStack(10);
        s.push(10);
        s.push(20);
        s.push(30);
        System.out.println(s.pop());
        System.out.println(s.pop());
        System.out.println(s.pop());
    }

    int[] data;
    int size;

    public ArrayStack(int size) {
        this.data = new int[size];
        size = 0;
    }

    public void push(int e) {
        if (size == this.data.length) {
            System.out.println("Stackoverflow");
            return;
        }
        this.data[this.size] = e;
        this.size++;
    }

    public int pop() {
        if (size == 0) {
            System.out.println("stack is empty");
            // return null;
            return -1;
        }
        this.size--;
        int top = this.data[this.size];
        this.data[this.size] = 0;
        return top;
    }

    public int peek() {
        if (size == 0) {
            System.out.println("stack is empty");
            // return null;
            return -1;
        }
        int top = this.data[this.size - 1];
        return top;
    }

}