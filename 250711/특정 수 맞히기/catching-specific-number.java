import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();

        while (a!=25) {
            if(a>25){
                System.out.println("Lower");
                a = sc.nextInt();
            }
            if(a<25){
                System.out.println("Higher");
                a = sc.nextInt();
            }
        }
        System.out.println("Good");
    }
}