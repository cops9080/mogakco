import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        String newStr = str.charAt(0) + "a" + str.substring(2, str.length()-2) + "a" + str.substring(str.length()-1, str.length());

        System.out.println(newStr);
    }
}