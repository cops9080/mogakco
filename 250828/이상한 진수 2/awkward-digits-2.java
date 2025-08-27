import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String binaryString = sc.next();
        
        int maxDecimalValue = 0;
        
        for (int i = 0; i < binaryString.length(); i++) {
            StringBuilder tempBinary = new StringBuilder(binaryString);
            
            char flippedChar;
            if (tempBinary.charAt(i) == '0') {
                flippedChar = '1';
            } else {
                flippedChar = '0';
            }
            tempBinary.setCharAt(i, flippedChar);
            
            int currentDecimalValue = Integer.parseInt(tempBinary.toString(), 2);
        
            if (currentDecimalValue > maxDecimalValue) {
                maxDecimalValue = currentDecimalValue;
            }
        }
        
        System.out.println(maxDecimalValue);
        sc.close();
    }
}