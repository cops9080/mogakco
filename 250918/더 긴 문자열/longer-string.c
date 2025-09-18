#include <stdio.h>
#include <string.h>

int main() {
    char s1[20];
    char s2[20];
    scanf("%s", s1);
    scanf("%s", s2);
    if (strlen(s1) > strlen(s2)) {
        printf("%s %d", s1, strlen(s1));
    } else if (strlen(s2) > strlen(s1)) {
        printf("%s %d", s2, strlen(s2));
    } else {
        printf("same");
    }
    return 0;
}