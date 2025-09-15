import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        char[] position = new char[100];

        for (int i = 0; i < n; i++) {
            int idx = sc.nextInt();
            position[idx] = sc.next().charAt(0);
        }

        int score = 0;
        int maxScore = 0;
        for (int i = 0; i < 100-k; i++) {
            for (int j = i; j < i+k+1; j++) {
                if (position[j] == 'G') {
                    score += 1;
                } else if (position[j] == 'H') {
                    score += 2;
                } else {
                    continue;
                }
            }
            maxScore = Math.max(maxScore, score);
            score = 0;
        }
        System.out.println(maxScore);
    }
}