import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> v = new ArrayList<>();
        String s;

        for (int i = 0; i<n; i++) {
            s = sc.next();
            if (s.equals("push_back")) {
                int a = sc.nextInt();
                v.add(a);
            }
            
            if (s.equals("get")) {
                int a = sc.nextInt();
                System.out.println(v.get(a-1));
            }
            
            if (s.equals("size")) {
                System.out.println(v.size());
            }
            
            if (s.equals("pop_back")) {
                v.remove(v.size()-1);
            }
        }



    }
}