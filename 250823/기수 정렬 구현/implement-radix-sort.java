import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int[] arr_new = new int[11];

        for (int i=0; i<n; i++) {
            int digit = arr[i];
            arr_new[digit] = arr[i];
        }

        for (int i=0; i<11; i++) {
            if (arr_new[i] != 0) {
                System.out.print(arr_new[i] + " ");
            }
        }
    }
}