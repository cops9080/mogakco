import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String str1 = sc.next();
        String str2 = sc.next();

        int length1 = str1.length();
        int length2 = str2.length();

        if (length1 > length2) {
            System.out.println(str1+" "+length1);
        } else if (length1 < length2) {
            System.out.println(str2+" "+length2);
        } else {
            System.out.println("same");
        }
    }
}