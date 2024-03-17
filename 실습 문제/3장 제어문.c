//
//  으뜸 파이썬 3장 제어문 관련 실습 문제
//
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(int argc, const char * argv[]) {
    /*
     LAB 3-A : if 조건문
     UTF-8은 켄 톰슨과 롭 파이크가 만든 문자 인코딩 방식입니다.
     다음과 같이 이진법 구조가 정해져 있습니다.
     1바이트 문자: 0xxxxxxx
     2바이트 문자: 110xxxxx 10xxxxxx
     3바이트 문자: 1110xxxx 10xxxxxx 10xxxxxx
     4바이트 문자: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
     참고로, 영어와 숫자 등 아스키코드는 1바이트, 한글은 3바이트 문자에 속합니다.
     파이썬에서 이진수 리터럴은 앞에 0b를 붙여서 적습니다.
     
     대화형 창에서 구조내 각 요소의 최소값과 최대값을 확인하면 다음과 같은 결과를 얻습니다.
     이진수                    십진수               구분
     0b0_0000000             0                  1바이트 문자
     0b0_1111111             127                1바이트 문자
     0b10_000000             128                2-4바이트 문자의 나머지 바이트
     0b10_111111             191                2-4바이트 문자의 나머지 바이트
     0b110_00000             192                2바이트 문자의 시작 바이트
     0b110_11111             223                2바이트 문자의 끝 바이트
     0b1110_0000             224                3바이트 문자의 시작 바이트
     0b1110_1111             239                3바이트 문자의 끝 바이트
     0b11110_000             240                4바이트 문자의 시작 바이트
     0b11110_111             247                4바이트 문자의 끝 바이트
     파이썬에서 숫자 앞에 0b를 붙이면 이진수로 인식합니다. 또한 숫자 중간에 _를 넣어서 가독성을 높일 수 있습니다.
     */
    
    // 문제: 유저로부터 0 ~ 255 범위의 정수를 입력 받아서 "leading byte of a 1-byte utf-8", "leading byte of a 2-byte utf-8", "leading byte of a 3-byte utf-8", "leading byte of a 4-byte utf-8", "continuation byte", "not utf-8", "out of range" 중 해당하는 문자열을 출력합니다.
    
    /* c 코드 */
    int byte;
    printf("Please enter an unsigned 1 byte number: ");
    
    /* 유저로부터 정수를 십진수 형식으로 입력 받음 */
    scanf("%d", &byte);
    
    /* UTF-8 구조의 어떤 부분에 해당하는지 범위 확인 */
    if(byte < 0b00000000 || byte > 0b11111111)
        printf("out of range");
    else if(byte <= 0b01111111)
        printf("leading byte of a 1-byte utf-8");
    else if(byte <= 0b10111111)
        printf("continuation byte");
    else if(byte <= 0b11011111)
        printf("leading byte of a 2-byte utf-8");
    else if(byte <= 0b11101111)
        printf("leading byte of a 3-byte utf-8");
    else if(byte <= 0b11110111)
        printf("leading byte of a 4-byte utf-8");
    else
        printf("not utf-8");

    printf("\n");
    
    
    /*
     LAB 3-B: for 반복문
     파이썬의 십진수 리터럴은 0과 0이 아닌수로 나눠서 정의됩니다.
     값이 0인 경우, 먼저 "0"이 나오고, 이어서 "_0" 또는 "0"이 반복될 수 있습니다. ex) 0, 0_0, 00, 0_0_0, 0_00
     값이 0이 아닌 경우, 먼저 0이 아닌 수가 나오고, 이어서 "_숫자" 또는 "숫자"가 반복될 수 있습니다. ex) 1, 1_2, 123
     이진수의 경우 먼저 "0b" 또는 "0B"가 나오고, 이어서 "_0또는1"이나 "0또는1"이 한번 이상 반복됩니다. ex) 0b0, 0b_1, 0b_0_1
     문제: 유저로부터 정수를 입력받았을 때 이진수인지, 십진수인지, 이에 해당하지 않는지를 판별합니다. "Binary", "Decimal", "Error" 중에 해당하는 문자열을 출력합니다.
     */
    
    /* c 코드 */
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
    printf("Please enter a number literal: ");
    
    /* 유저로부터 정수 리터럴을 입력 받음 */
    char str[100];
    scanf("%99s", str);
    
    /* 첫글자가 0이 아닌 정수로 시작할 때 숫자 또는 _숫자가 이어서 반복적으로 나올 수 있음 */
    if (str[0] > '0' && str[0] <= '9')
    {
        int i = 1;
        for (i = 1; i < 100; i++)
        {
            if (str[i] == 0)
            {
                printf("Decimal");
                break;
            }
            else if (str[i] >= '0' && str[0] <= '9')
            {
                continue;
            }
            else if (str[i] == '_')
            {
                if (++i < 100 && str[i] >= '0' && str[i] <= '9')
                {
                    continue;
                }
                else
                {
                    printf("Error");
                    break;
                }
            }
            else
            {
                printf("Error");
                break;
            }
        }
    }

    /* 첫글자가 0으로 시작할 때 */
    else if (str[0] == '0')
    {
        /* str == "0" */
        if (str[1] == 0)
            printf("Decimal");
        
        /* str == "00", "0_0", ... */
        else if (str[1] == '0' || str[1] == '_')
        {
            int i;
            for (i = 2; i < 100; i++)
            {
                if (str[i] == 0)
                {
                    printf("Decimal");
                    break;
                }
                else if (str[i] == '0')
                    continue;
                /* "_"이 있으면 다음 문자는 반드시 숫자여야됨 */
                else if (str[i] == '_')
                {
                    if (++i < 100 && str[i] == '0')
                        continue;
                    else
                    {
                        printf("Error");
                        break;
                    }
                }
                /* 0을 나타내는 십진수는 "0", "_"만으로 이루어짐 */
                else
                {
                    printf("Error");
                    break;
                }
            }
            printf("Error");
        }
        
        /* str == "0b1", "0B_01", "0b_101", ... */
        else if (str[1] == 'b' || str[1] == 'B')
        {
            int i = 2;
            /* "0b" 후에 "숫자" 또는 "_숫자"가 반드시 있어야 됨 */
            if (str[i] == '0' || str[i] == '1' \
                || (str[i++] == '_' && (str[i] == '0' || str[i] == '1')))
            {
                for(i++; i < 100; i++)
                {
                    if (str[i] == 0)
                    {
                        printf("Binary");
                        break;
                    }
                    else if (str[i] == '0' || str[i] == '1')
                        continue;
                    
                    else if (str[i] == '_')
                    {
                        if (++i < 100 && (str[i] == '0' || str[i] == '1'))
                            continue;
                        else
                        {
                            printf("Error");
                            break;
                        }
                    }
                    else
                    {
                        printf("Error");
                        break;
                    }
                }
            }
            /* (0b 또는 0B) 후에 (이진수 숫자 또는 _이진수 숫자)가 없을 때 */
            else
                printf("Error");
        }
        /* 첫글자가 0인데, 두번째 글자가 0, _, b, B가 아닐 때 */
        else
            printf("Error");
    }
    /* 첫글자가 숫자가 아닐 때 */
    else
        printf("Error");
        
    printf("\n");
    
    return 0;
}


/* 출처
 LAB 3-A: https://ko.wikipedia.org/wiki/UTF-8
 LAB 3-B: https://docs.python.org/ko/3/reference/lexical_analysis.html#integer-literals
 */
