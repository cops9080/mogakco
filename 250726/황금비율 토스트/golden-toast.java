import java.util.Scanner;
import java.util.ListIterator;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Character> l = new LinkedList<>();

        int n = sc.nextInt();
        int m = sc.nextInt();
        String s = sc.next();
        sc.nextLine();
        
        for (int i=0; i<s.length(); i++) {
            l.add(s.charAt(i));
        }

        ListIterator<Character> it = l.listIterator(l.size());

        for (int i = 0; i < m; i++) {
            String command = sc.nextLine();
            if (command.equals("L")) {
                if (it.hasPrevious()) {
                    it.previous();
                }
            }
            if (command.equals("R")) {
                if (it.hasNext()) {
                    it.next();
                }
            }
            if (command.equals("D")) {
                if (it.hasNext()) {
                    it.next();
                    it.remove();   
                }
            }
            if (command.startsWith("P")) {
                char sP = command.charAt(2);
                it.add(sP);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char c : l) {
            sb.append(c);
        }
        System.out.println(sb.toString());
        
    }
}