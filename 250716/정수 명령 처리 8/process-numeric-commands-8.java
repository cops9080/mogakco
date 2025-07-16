import java.util.Scanner;
import java.util.LinkedList;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> l = new LinkedList<>();

        int n = sc.nextInt();
        int a;
        for (int i = 0; i < n; i++) {
            String command = sc.next();
            if (command.equals("push_front")) {
                a = sc.nextInt();
                l.addFirst(a);
            }
            if (command.equals("push_back")) {
                a = sc.nextInt();
                l.addLast(a);
            }
            if (command.equals("pop_front")) {
                System.out.println(l.pollFirst());
            }
            if (command.equals("pop_back")) {
                System.out.println(l.pollLast());
            }
            if (command.equals("size")) {
                System.out.println(l.size());
            }
            if (command.equals("empty")) {
                if (l.isEmpty()==true) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
                
            }
            if (command.equals("front")) {
                System.out.println(l.peekFirst());
            }
            if (command.equals("back")) {
                System.out.println(l.peekLast());
            }
        }
    }
}