#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int k = 0; k < 2; k++) {
        for (int i = 0; i < n; i++) {  
            for (int j = 0; j < n; j++) {
                printf("*");
            }
            printf("\n");
        }
        printf("\n");
    }
        
    return 0;
}