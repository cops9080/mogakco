#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    while (N != 0) {
        printf("%d\n", N);
        N /= M;
    }
    
    return 0;
}