import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.print(a+" ");

        while (a<=b) {
            if (a%2==1) {
                a = a*2;
                if (a>b) {
                    break;
                }       
                System.out.print(a+" ");
            } else {  
                a = a+3;
                if (a>b) {
                    break;
                }
                System.out.print(a+" ");
            }
        }
    }
}