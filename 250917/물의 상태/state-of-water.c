#include <stdio.h>

int main() {
    int tmp;
    scanf("%d", &tmp);

    if (tmp < 0) {
        printf("ice");
    } else if (tmp >= 100) {
        printf("vapor");
    } else {
        printf("water");
    }
    return 0;
}