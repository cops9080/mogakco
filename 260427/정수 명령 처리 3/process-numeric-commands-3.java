import java.util.*;

public class Main {
    public static void main(String[] args) {
        Deque<Integer> deque = new ArrayDeque<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        sc.nextLine();

        while (n-->0) {
            String command = sc.nextLine();

            if (command.startsWith("push_front")) {
                deque.addFirst(Integer.parseInt(command.split(" ")[1]));
            }
            else if (command.startsWith("push_back")) {
                deque.addLast(Integer.parseInt(command.split(" ")[1]));
            }
            else if (command.equals("pop_front")) {
                System.out.println(deque.pollFirst());
            }
            else if (command.equals("pop_back")) {
                System.out.println(deque.pollLast());
            }
            else if (command.equals("size")) {
                System.out.println(deque.size());
            }
            else if (command.equals("empty")) {
                System.out.println(deque.isEmpty() ? "1" : "0");
            }
            else if (command.equals("front")) {
                System.out.println(deque.peekFirst());
            }
            else if (command.equals("back")) {
                System.out.println(deque.peekLast());
            }
            else {
                return;
            }
        }

    }
}