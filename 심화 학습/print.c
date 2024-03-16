//
//  파이썬 print 함수를 C로 비슷하게 구현
//  reference: https://stackoverflow.com/questions/67629921/print-combine-generic-and-variadic-functions
//  Created by 1 on 3/15/24.
//

#include <stdio.h>

char* sep = " ";
char* end = "\n";

#define print(...) print_max8(__VA_ARGS__, 8, 7, 6, 5, 4, 3, 2, 1, 0);

#define print_max8(a0, a1, a2, a3, a4, a5, a6, a7, COUNT, ...) \
{ \
if (COUNT > 0) print_1(a0); printf("%s", sep); \
if (COUNT > 1) print_1(a1); printf("%s", sep); \
if (COUNT > 2) print_1(a2); printf("%s", sep); \
if (COUNT > 3) print_1(a3); printf("%s", sep); \
if (COUNT > 4) print_1(a4); printf("%s", sep); \
if (COUNT > 5) print_1(a5); printf("%s", sep); \
if (COUNT > 6) print_1(a6); printf("%s", sep); \
if (COUNT > 7) print_1(a7); printf("%s", sep); \
printf("%s", end); \
}

#define print_1(x) \
        printf( \
          _Generic( (x), int:"%d", double:"%g", char*:"%s" ) \
          , x)

int main(int argc, const char * argv[]) {
    // insert code here...
    print("Hello, print!", 1, 2.3);
    return 0;
}
