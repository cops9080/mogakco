#include <stdio.h>

int main() {
    int a = 1;
    int b = 5;
    int c = 3;

    a = c;
    a = a + c;
    b = b - c;

    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", c);

    return 0;
}