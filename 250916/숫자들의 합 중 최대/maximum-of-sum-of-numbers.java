import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        int sumVal = 0;
        int maxVal = 0;
        int num = 0;
        for (int i = x; i <= y; i++) {
            num = i;
            while(num > 0) {
                sumVal += num % 10;
                int mok = num / 10;
                num = mok;
                }
            maxVal = Math.max(maxVal, sumVal);
            sumVal = 0;
        }
        System.out.println(maxVal);
    }
}