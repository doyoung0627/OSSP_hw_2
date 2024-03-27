이름 : 이도영

학번 : 2022113175

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    char a[50];
    int b;
    printf("이름을 입력하세요: ");
    scanf("%s", & a);
    printf("학번을 입력하세요: ");
    scanf("%d", & b);
    printf("\n<출력>");
    printf("\n이름: %s", a);
    printf("\n학번: %d", b);
    return 0;
}


