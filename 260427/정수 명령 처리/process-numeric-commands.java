import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> stack = new Stack<>();
        sc.nextLine();
        while (n-->0) {
            String command = sc.nextLine();

            if (command.startsWith("push")) {
                int a = Integer.parseInt(command.split(" ")[1]);
                stack.push(a);
            }
            else if (command.equals("size")) {
                System.out.println(stack.size());
            }
            else if (command.equals("empty")) {
                System.out.println(stack.isEmpty() ? "1" : "0");
            }
            else if (command.equals("pop")) {
                System.out.println(stack.pop());
            }
            else if (command.equals("top")) {
                System.out.println(stack.peek());
            }
            else {
                return;
            }
        }
    }
}