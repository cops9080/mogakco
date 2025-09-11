import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int total = 0;
        int maxTotal = 0;
        for (int i = 0; i <= n-k; i++) {
            for (int j = i; j < i+k; j++) {
                total += arr[j];
            }
            if (total > maxTotal) {
                maxTotal = total;
            }
            total = 0;
        }

        System.out.println(maxTotal);
    
    }
}