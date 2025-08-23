import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        radixSort(arr);

        // 결과 출력
        for (int x : arr) {
            System.out.print(x + " ");
        }
    }

    static void radixSort(int[] arr) {
        int max = getMax(arr);

        // 1의 자리, 10의 자리, 100의 자리 ... 순으로 정렬
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSortByDigit(arr, exp);
        }
    }

    static void countingSortByDigit(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10]; // 0~9 버킷

        // 해당 자리수의 숫자 카운팅
        for (int i = 0; i < n; i++) {
            int digit = (arr[i] / exp) % 10;
            count[digit]++;
        }

        // 누적합으로 변환
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        // 안정 정렬 (뒤에서부터 순회)
        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }

        // 원본 배열에 복사
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }

    static int getMax(int[] arr) {
        int max = arr[0];
        for (int x : arr) {
            if (x > max) max = x;
        }
        return max;
    }
}
