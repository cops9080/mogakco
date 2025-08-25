import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();
        int C = sc.nextInt();
        char[][] grid = new char[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                grid[i][j] = sc.next().charAt(0);
            }
        }

        int idx = 0;
        int jump = 0;
        int successCnt = 0;
        for (int i=0; i<R-1; i++) {
            for (int k=0; k<C-i; k++) {
                    char beforeJump = grid[i][k];
                for (int j=0; j<C-1; j++) {
                    if (beforeJump != grid[i+1][j+1]) {
                        jump++;
                    }
                }
                if (jump == 2) {
                    successCnt += 1;
                    jump = 0;
                }
            }
        }

        if (grid[0][0] == grid[R-1][C-1]) {
            System.out.print(0);
        } else {
            System.out.print(successCnt);
        }
    }
}