#include <stdio.h>

int main() {
    int mathA, engA, mathB, engB;
    scanf("%d %d", &mathA, &engA);
    scanf("%d %d", &mathB, &engB);

    if (mathA > mathB && engA > engB) {
        printf("1");
    } else {
        printf("0");
    }
    return 0;
}