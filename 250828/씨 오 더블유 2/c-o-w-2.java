import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();
        
        int cnt = 0;
        for (int c=0; c<str.length(); c++) {
            char ch_c = str.charAt(c);
            if (ch_c != 'C') {
                continue;
            }
            for (int o=c+1; o<str.length(); o++) {
                char ch_o = str.charAt(o);
                if (ch_o != 'O') {
                    continue;
                }
                for (int w=o+1; w<str.length(); w++) {
                    char ch_w = str.charAt(w);
                    if (ch_w != 'W') {
                        continue;
                    } else {
                        cnt++;
                    }
                }
            }
        }

        System.out.print(cnt);
    }
}