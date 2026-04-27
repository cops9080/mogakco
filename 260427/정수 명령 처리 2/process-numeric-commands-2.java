import java.util.*;

public class Main {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        sc.nextLine();
        
        while (n-->0) {
            String command = sc.nextLine();

            if (command.startsWith("push")) {
                queue.add(Integer.parseInt(command.split(" ")[1]));
            }
            else if (command.equals("pop")) {
                System.out.println(queue.poll());
            }
            else if (command.equals("size")) {
                System.out.println(queue.size());
            }
            else if (command.equals("empty")) {
                System.out.println(queue.isEmpty() ? "1" : "0");
            }
            else if (command.equals("front")) {
                System.out.println(queue.peek());
            }
            else { return; }
        }
    }
}