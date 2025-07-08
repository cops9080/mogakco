import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strArr = {"apple", "banana", "grape", "blueberry", "orange"};

        String str = sc.next();
        int cnt = 0;

        for (int i=0; i<5; i++) {
            if ((strArr[i].charAt(2)==str.charAt(0))||(strArr[i].charAt(3)==str.charAt(0))) {
                System.out.println(strArr[i]);
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}