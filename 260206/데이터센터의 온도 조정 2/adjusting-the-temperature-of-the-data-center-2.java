import java.util.Scanner;
public class Main {
    public static int maxWorkLoad = 0;
    public static int workload(int temp, int ta, int tb, int c, int g, int h) {
        if (temp < ta) {
            return c;
        } else if (temp >= ta && temp < tb) {
               return g;
        } else {
            return h;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int c = sc.nextInt();
        int g = sc.nextInt();
        int h = sc.nextInt();
        int[] ta = new int[n];
        int[] tb = new int[n];

        for (int i = 0; i < n; i++) {
            ta[i] = sc.nextInt();
            tb[i] = sc.nextInt();    
        }
        for (int t = 0; t <= 1000; t++) {
            int totalWorkLoad = 0;
            for (int j = 0; j < n; j++) {
                totalWorkLoad += workload(t, ta[j], tb[j], c, g, h);
            }
            maxWorkLoad = Math.max(maxWorkLoad, totalWorkLoad);
        }
        System.out.println(maxWorkLoad);
            
    }
}