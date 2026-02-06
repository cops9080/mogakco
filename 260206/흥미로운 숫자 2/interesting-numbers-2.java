import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();

        

        int differentCount = 0;
        int interestingCount = 0;
        for (int i = x; i <= y; i++) {
            differentCount = 0;
            // 숫자 n이 몇 번 등장 했는지를 담을 배열 0~9
            int[] number = new int[10];

            String numStr = i + "";
            for (int j = 0; j < numStr.length(); j++) {
                int idx = (int)(numStr.charAt(j)) - 48;
                number[idx]++;
            }
            for (int j = 0; j < 10; j++) {
                if (differentCount > 2) {
                    break;
                }
                int a = number[j];
                if (a != 0) {
                    differentCount++;
                }
            }
            if (differentCount == 2) {
                int overTwo = 0;
                for (int k = 0; k < 10; k++) {
                    if (overTwo == 2) {
                        break;
                    }
                    if (number[k] >= 2) {
                        overTwo++;
                    }
                }
                if (overTwo == 1) {
                    interestingCount++;
                }
            }
        }
        System.out.println(interestingCount);
    }
}