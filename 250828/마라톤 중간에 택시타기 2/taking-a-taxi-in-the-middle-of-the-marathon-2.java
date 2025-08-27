import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        
        int minTaxiDistance = Integer.MAX_VALUE;
        int taxiDistance = 0;
        //스킵할 체크포인트 설정
        for (int i=1; i<n-1; i++) {
            int skipPoint_X = x[i];
            int skipPoint_Y = y[i];
            //System.out.println("skipPoint_X : " + skipPoint_X);
            //System.out.println("skipPoint_Y : " + skipPoint_Y);
            //System.out.println();
            //택시 거리 계산
            int lastVisitedIndex = 0;
            for (int j=0; j<n; j++) {
                //거리를 계산할 체크포인트가 스킵할 포인트일 시 건너뛰기 
                if (i == j) {
                    continue;
                } else {
                    //System.out.println("x[j] : " + x[j]);                    
                    //System.out.println("x[j+1] : " + x[lastVisitedIndex]);                    
                    //System.out.println("y[j] : " + y[j]);                    
                    //System.out.println("y[j+1] : " + y[lastVisitedIndex]);
                    //System.out.println();                                                                                                    
                    taxiDistance += Math.abs(x[j]-x[lastVisitedIndex]) + Math.abs(y[j]-y[lastVisitedIndex]);
                    lastVisitedIndex = j;
                }
            }
            if (minTaxiDistance > taxiDistance) {
                minTaxiDistance = taxiDistance;
            }
            //System.out.println("taxiDistance : " + taxiDistance);
            //System.out.println();
            taxiDistance = 0;
        }
        System.out.println(minTaxiDistance);
    }
}