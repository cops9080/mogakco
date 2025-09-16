import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int sumVal = 0;
        int maxVal = 0;
        int cnt = 0;

        for(int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {

                //부분수열의 합 계산
                sumVal = 0;
                for (int k = i; k <= j; k++) {
                    sumVal += arr[k];
                }
                
                int length = j - i + 1;
                
                double mean = (double)sumVal / length;
                
                
                boolean found = false;
                for (int k = i; k <= j; k++) {
                    if (arr[k] == mean) {
                        found = true;
                        break;
                    }
                }

                if (found) {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}