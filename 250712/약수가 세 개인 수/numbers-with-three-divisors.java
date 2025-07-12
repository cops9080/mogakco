import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int start = sc.nextInt();
        int end = sc.nextInt();
        int cnt2 = 0;

        for (int i = start; i <= end; i++) {
            int cnt1 = 0;
            
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) cnt1++;
            }

            if (cnt1 == 3) {
                cnt2++;
            }
        }
        System.out.print(cnt2);
    }
}
