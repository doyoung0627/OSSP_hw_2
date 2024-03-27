#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
    char a[50];
    int b;
    char c[50];
    printf("이름을 입력하세요: ");
    scanf("%s", & a);
    printf("학번을 입력하세요: ");
    scanf("%d", & b);
    printf("팀 이름을 입력하세요: ");
    scanf("%s", &c);
    printf("\n<출력>");
    printf("\n이름: %s", a);
    printf("\n학번: %d", b);
    printf("\n팀 이름: %s", c);
    return 0;
}
