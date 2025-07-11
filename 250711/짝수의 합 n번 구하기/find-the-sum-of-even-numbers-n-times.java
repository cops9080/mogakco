import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;
        int[][] arr = new int[n][2];

        for (int i=0; i<n; i++) {
            for (int j=0; j<2; j++) {
                arr[i][j] = sc.nextInt();
                
            }
        }

        for (int i=0; i<n; i++) {
            
                for (int j=arr[i][0]; j<=arr[i][1]; j++) {
                    if (j%2==0) {
                        sum = sum + j;
                    }
                }
            System.out.println(sum);
            sum = 0;
        }


    }
}