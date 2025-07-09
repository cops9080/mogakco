import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> v = new ArrayList<>();
        
        int n = sc.nextInt();
        int a;

        String cmd;

        for (int i = 0; i < n; i++) {
            cmd = sc.next();
            if (cmd.equals("push_back")) {
                a = sc.nextInt();
                v.add(a);
                // System.out.println(a);
            }
            if (cmd.equals("pop_back")) {
                v.remove(v.size()-1);
                // System.out.println(v.get(i));
            }
            if (cmd.equals("size")) {
                System.out.println(v.size());
            }
            if (cmd.equals("get")) {
                a = sc.nextInt();
                System.out.println(v.get(a-1));
            }          
        }
    }
}