#include <stdio.h>

int main() {
    char arr[10];
    char c;

    for (int i = 0; i < 10; i++) {
        scanf(" %c", &c);
        arr[i] = c;
    }
    for (int i = 9; i >= 0; i--) {
        printf("%c", arr[i]);
    }
    return 0;
}