#include <stdio.h>

int main() {
    int a, b, total;
    double avg;

    scanf("%d %d", &a, &b);
    
    total = a + b;
    avg = (double) total / 2;
    printf("%d %.1lf", total, avg);
    return 0;
}