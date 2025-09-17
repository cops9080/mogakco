#include <stdio.h>

int main() {
    int a, b, c;
    int total, avg;

    scanf("%d %d %d", &a, &b, &c);
    
    total = a + b + c;
    avg = total / 3;
    printf("%d\n", total);
    printf("%d\n", avg);
    printf("%d\n", total - avg);
    return 0;
}