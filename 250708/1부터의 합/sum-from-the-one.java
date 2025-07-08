import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;
        int count = 0;

        for(int i=1; i<=n; i++){
            if (sum>n) {
                break;
            }
            sum = sum + i;
            count++;
        }
        System.out.println(count);
    }
}