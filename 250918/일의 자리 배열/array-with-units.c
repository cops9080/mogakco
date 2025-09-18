#include <stdio.h>

int main() {
    int a, b;
    int arr[10];
    scanf("%d %d", &a, &b);

    arr[0] = a;
    arr[1] = b;
    for (int i = 0; i < 8; i++) {
        arr[i+2] = (arr[i] + arr[i+1]) % 10;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}