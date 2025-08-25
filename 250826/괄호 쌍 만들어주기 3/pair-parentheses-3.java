import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        int cnt = 0;
        for (int i=0; i<str.length(); i++) {
            char open = str.charAt(i);
            if (open == '(') {
                for (int j=i+1; j<str.length(); j++) {
                    char close = str.charAt(j);
                    if (close == ')') {
                        cnt++;
                    }
                }
            }
        }
        System.out.print(cnt);
    }
}