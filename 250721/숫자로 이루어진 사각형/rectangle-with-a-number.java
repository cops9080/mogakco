import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        printS(n);
    }

    public static void printS(int n) {
        int c = 1;
        for (int i=0; i<n; i++) {
            for (int j=1; j<=n; j++) {
                if (c==10) c=1;
                System.out.print(c+" ");
                c++;
            }
            System.out.println();
        }
    }
}