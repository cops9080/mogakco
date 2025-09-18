#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    scanf("%s", s);
    s[1] = 'a';
    s[strlen(s)-2] = 'a';

    printf("%s", s);
    return 0;
}