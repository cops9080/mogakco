import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        long total = 0;

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
            total += A[i];
        }

        // 가중치 중앙값 찾기
        long prefix = 0;
        int median = 0;
        for (int i = 0; i < N; i++) {
            prefix += A[i];
            if (prefix * 2 >= total) { // 절반 이상 모이면 해당 위치
                median = i;
                break;
            }
        }

        // 최소 이동 거리 계산
        long answer = 0;
        for (int i = 0; i < N; i++) {
            answer += (long) A[i] * Math.abs(i - median);
        }

        System.out.println(answer);
    }
}
