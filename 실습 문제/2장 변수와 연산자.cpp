// Ch2_variable_and_operator.cpp
// 2장 변수와 연산자 LAB 문제의 C++, C 솔루션입니다. 

#include <iostream>  // std::cout
#include <cmath>     // std::pow
#include <complex>   // std::complex
#include <string>    // std::string
#include <stdio.h>   /* printf */
#include <math.h>    /* pow */

int main()
{
    std::cout << "\nLAB 2-1\n";
    // LAB 2-1 : 여러 자료형의 값을 화면에 출력하기
    // 
    // Hello World!를 화면에 출력합니다.
    std::cout << "Hello World!\n"; // C++
    printf("Hello World!\n"); // C
    //
    // 오늘 날짜를 "Today is {month} / {day} ." 형식으로 화면에 출력합니다.
    std::cout << "Today is " << 3 << " / " << 13 << " .\n"; // C++
    printf("Today is %d / %d .\n", 3, 13); // C
    // 
    // 계산 결과를 "1 plus 1 equals to {1+1} " 형식으로 화면에 출력합니다.
    std::cout << "1 plus 1 equals to " << 1 + 1 << std::endl; // C++
    printf("1 plus 1 equals to %d\n", 1 + 1); // C
    //

    std::cout << "\nLAB 2-2\n";
    // LAB 2-2 : 영수증 계산하기
    // 주어진 메뉴판에서 포테이토 피자 5판과 스테이크 피자 2판의 가격, 
    // 부가세 10%가 더해진 총 금액을 다음과 같은 형식으로 출력합니다.  
    // """
    // Potato pizza 5: #potato_pizza_price
    // Steak pizza 2: #stake_pizza_price
    // Total: #total_price
    // """ 
    // =====메뉴판=====
    // 포테이토 피자      15,000
    // 스테이크 피자      25,000
    std::cout << "Potato pizza 5: " << (15000 * 5) << std::endl;
    std::cout << "Steak pizza 2: " << (25000 * 2) << std::endl;
    std::cout << "Total: " << (int)((15000 * 5 + 25000 * 2) * (1 + 0.10)) << std::endl; // C++
    printf("Potato pizza 5: %d\nSteak pizza 2: %d\nTotal: %d\n",
        15000 * 5, 25000 * 2,
        (int)((15000 * 5 + 25000 * 2) * (1 + 0.10))); // C
    //

    std::cout << "\nLAB 2-3\n";
    // LAB 2-3 : 변수를 써서 영수증 계산하기 (LAB 2-2와 이어집니다.)
    // 포테이토 피자와 스테이크 피자 가격을 변수 price_potato_pizza, price_steak_pizza에 저장하고,
    // 포테이토 피자 5판, 스테이크 피자 2판의 가격을 
    // 변수 price_potato_pizza_total, price_steak_pizza_total에 저장합니다. 
    // 총 금액에 부가서 10%를 더해서 변수 price_total에 저장합니다. 
    int price_potato_pizza = 15000, price_steak_pizza = 25000,
        price_potato_pizza_total = price_potato_pizza * 5,
        price_steak_pizza_total = price_steak_pizza * 2,
        price_total = (int)((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10));

    std::cout << "\nLAB 2-3-1\n";
    // 1. 정의한 변수를 써서 LAB 2-2에서와 같이 화면에 영수증을 출력합니다.
    std::cout << "Potato pizza 5: " << price_potato_pizza_total
        << "\nSteak pizza 2: " << price_steak_pizza_total
        << "\nTotal: " << price_total << std::endl; // C++ 출력
    printf("Potato pizza 5: %d\nSteak pizza 2: %d\nTotal: %d\n",
        price_potato_pizza_total, price_steak_pizza_total, price_total); // C 출력

    std::cout << "\nLAB 2-3-2\n";
    // 2. 포테이토 피자의 가격을 30% 할인받았을 때, 영수증의 Potato pizza 5 값과 Total 값을 변경하여 출력합니다.
    price_potato_pizza = (int)(price_potato_pizza * (1 - 0.30));
    price_potato_pizza_total = price_potato_pizza * 5;
    price_total = (int)((price_potato_pizza_total + price_steak_pizza_total) * (1 + 0.10));

    std::cout << "Potato pizza 5: " << price_potato_pizza_total
        << "\nSteak pizza 2: " << price_steak_pizza_total
        << "\nTotal: " << price_total << std::endl; // C++ 출력
    printf("Potato pizza 5: %d\nSteak pizza 2: %d\nTotal: %d\n",
        price_potato_pizza_total, price_steak_pizza_total, price_total); // C 출력

    std::cout << "\nLAB 2-3-3\n";
    // 3. 추가로 총 금액에서 20% 할인 혜택을 받은 경우에, 영수증의 Total 값을 변경하여 출력합니다.
    price_total = (int)(price_total * (1 - 0.20));
    std::cout << "Potato pizza 5: " << price_potato_pizza_total
        << "\nSteak pizza 2: " << price_steak_pizza_total
        << "\nTotal: " << price_total << std::endl; // C++ 출력
    printf("Potato pizza 5: %d\nSteak pizza 2: %d\nTotal: %d\n",
        price_potato_pizza_total, price_steak_pizza_total, price_total); // C 출력

    std::cout << "\nLAB 2-4\n";
    // LAB 2-4 : 여러 자료형의 변수를 써서 영수증 출력하기 (LAB 2-3와 이어집니다.)
    // 포테이토 피자의 영수증에 출력되는 영문명 "Potato pizza"를 변수 name_potato_pizza에 저장합니다.
    // 스테이크 피자의 영수증에 출력되는 영문명 "Steak pizza"를 변수 name_steak_pizza에 저장합니다. 
    // 총 금액이 영수증에 출력되는 영문명 "Total"을 변수 name_total에 저장합니다.
    // 포테이토 피자 주문 수량을 변수 amount_potato_pizza에 저장합니다. 
    // 스테이크 피자 주문 수량을 변수 amount_steak_pizza에 저장합니다. 
    // 생성한 변수를 이용해서 영수증을 출력합니다.  

    const char* name_potato_pizza = "Potato pizza", * name_steak_pizza = "Steak pizza",
        * name_total = "Total";
    int amount_potato_pizza = 5, amount_steak_pizza = 2;
    std::cout << name_potato_pizza << " " << amount_potato_pizza << ": " << price_potato_pizza_total << "\n"
        << name_steak_pizza << " " << amount_steak_pizza << ": " << price_potato_pizza_total << "\n"
        << name_total << ": " << price_total << "\n"; // C++ 출력
    printf("%s %d: %d\n%s %d: %d\n %s: %d\n", name_potato_pizza, amount_potato_pizza, price_potato_pizza_total,
        name_steak_pizza, amount_steak_pizza, price_steak_pizza_total, name_total, price_total); // C 출력

    std::cout << "\nLAB 2-5\n";
    // LAB 2-5 : 변수 이름의 오류 찾기
    // 다양한 종류의 오류를 찾고 고쳐봅니다.

    std::cout << "\nLAB 2-5-1\n";
    // 1. 변수 이름으로 파이썬에서 키워드로 지정된 단어를 썼을 때
    // 다음 주석처리된 코드가 오류 없이 동작하게 변수 이름을 바꿔보세요
    // int true = 1;
    // std::cout << true << std::endl;
    // printf("%d\n", true);
    int True = 1;
    std::cout << True << std::endl; // C++ 출력
    printf("%d\n", True); // C 출력

    std::cout << "\nLAB 2-5-2\n";
    // 2. 변수 이름에 오타가 있을 때
    // 다음 주석처리된 코드가 오류 없이 동작하게 변수 이름을 바꿔보세요
    // const char* name_steaky_pizza = "Steaky pizza";
    // std::cout << Name_steaky_pizza << std::endl;
    // printf("%s\n", Name_steaky_pizza);
    const char* name_steaky_pizza = "Steaky pizza";
    std::cout << name_steaky_pizza << std::endl; // C++ 출력
    printf("%s\n", name_steaky_pizza); // C 출력

    std::cout << "\nLAB 2-5-3\n";
    // 3. 변수 이름에 의미가 없을 때
    // 다음 주석처리된 코드에서 변수 이름을 변수 내용과 관련있게 지어서 바꿔보세요
    // int abcdefghijklmnop = 251;
    // std::cout << "Your order number is " << abcdefghijklmnop << "." << std::endl;
    // printf("Your order number is %d.\n", abcdefghijklmnop);
    int order_num = 251;
    std::cout << "Your order number is " << order_num << "." << std::endl; // C++ 출력
    printf("Your order number is %d.\n", order_num); // C 출력


    std::cout << "\nLAB 2-5-4\n";
    // 4. 변수 이름이 너무 길 때
    // 다음 주석처리된 코드에서 변수 이름을 짧게 바꿔보세요
    // const char* pizza_delivery_reciept_string_for_this_pizza_order = "Total: 10,000 won";
    // std::cout << pizza_delivery_reciept_string_for_this_pizza_order << std::endl;
    // printf("%s\n",pizza_delivery_reciept_string_for_this_pizza_order);
    const char* reciept = "Total: 10,000 won"; // C++ 출력
    std::cout << reciept << std::endl; // C 출력
    printf("%s\n", reciept);

    std::cout << "\nLAB 2-5-5\n";
    // 5. 변수 이름이 변수 내용과 다른 의미를 나타낼 때
    // 다음 주석처리된 코드에서 변수 이름을 변수 내용과 의미가 맞게 바꿔보세요
    // int price = 10000;
    // int amount = 2;
    // double tax = 0.1;
    // int price_total_without_tax = price * amount + (int) (price * amount * tax);
    // std::cout << price_total_without_tax << std::endl;
    // printf("%d\n", price_total_without_tax);
    int price = 10000;
    int amount = 2;
    double tax = 0.1;
    int price_total_with_tax = price * amount + (int)(price * amount * tax);
    std::cout << price_total_with_tax << std::endl; // C++ 출력
    printf("%d\n", price_total_with_tax); // C 출력

    std::cout << "\nLAB 2-5-6\n";
    // 6. 변수 이름에 허용되지 않는 문자가 있을 때
    // 다음 주석처리된 코드에서 변수 이름을 허용되는 문자만 사용해서 바꿔보세요
    // int price_+_tax = 10000 + 10000 * 0.10;
    // std::cout << price_+_tax << std::endl;
    // printf("%d\n", price_+_tax);
    int price_with_tax = (int)(10000 + 10000 * 0.10);
    std::cout << price_with_tax << std::endl; // C++ 출력
    printf("%d\n", price_with_tax); // C 출력

    std::cout << "\nLAB 2-6\n";
    // LAB 2-6 : 변수 값을 다시 저장하기
    // 변수 num, result에 각각 0을 저장합니다.
    // num에 1을 저장합니다.
    // result + num의 결과를 result에 저장하고 출력합니다.
    double num = 0, result = 0;
    num = 1;
    result = result + num;
    std::cout << num << std::endl; // C++ 출력
    printf("%f\n", num); // C 출력

    std::cout << "\nLAB 2-7\n";
    // LAB 2-7 : 산술연산자 써보기 (LAB 2-6에서 이어집니다)
    // result에 0을 저장합니다.
    // 변수 num_left에 6을 저장합니다.
    // 변수 num_right에 6을 저장합니다.
    // num_left * num_right의 결과를 result에 저장하고 출력합니다.
    // num_left에 result를 저장합니다.
    // num_right에 0.5을 저장합니다.
    // num_left ** num_right의 결과를 result에 저장하고 출력합니다.
    // num_left에 result를 저장합니다.
    // num_right에 5를 저장합니다.
    // num_left % num_right의 결과를 result에 저장하고 출력합니다.
    // num_left에 6을 저장합니다.
    // num_right에 5를 저장합니다.
    // num_left // num_right의 결과를 result에 저장하고 출력합니다.
    // num_left에 6을 저장합니다.
    // num_right에 5를 저장합니다.
    // num_left / num_right의 결과를 result에 저장하고 출력합니다.
    result = 0;
    double num_left = 6;
    double num_right = 6;
    std::cout << (result = num_left * num_right) << std::endl; // C++ 출력
    printf("%f\n", result = num_left * num_right); // C 출력
    num_left = result;
    num_right = 0.5;
    std::cout << (result = std::pow(num_left, num_right)) << std::endl; // C++ 출력
    printf("%f\n", result = pow(num_left, num_right)); // C 출력
    num_left = result;
    num_right = 5;
    std::cout << (result = (int)num_left % (int)num_right) << std::endl; // C++ 출력
    printf("%f\n", result = (int)num_left % (int)num_right); // C 출력
    num_left = 6;
    num_right = 5;
    std::cout << (result = (int)num_left / (int)num_right) << std::endl; // C++ 출력
    printf("%f\n", result = (int)num_left / (int)num_right); // C 출력
    num_left = 6;
    num_right = 5;
    std::cout << (result = num_left / num_right) << std::endl; // C++ 출력
    printf("%f\n", result = num_left / num_right); // C 출력

    std::cout << "\nLAB 2-8\n";
    // LAB 2-8 : 복소수 연산 해보기
    // 복소수 연산 (1 + 1i) + (1 + 1i), (1 + 1i) - (1 + 1i), (1 + 1i) * (1 + 1i), (1 + 1i) / (1 + 1i) 결과를 출력하시오 
    using std::literals::complex_literals::operator""i;
    std::complex<double> x = 1.0 + 1i;
    std::complex<double> y = 1.0 + 1i;
    std::cout << x + y << x - y << x * y << x / y << std::endl; // C++ 출력

    std::cout << "\nLAB 2-9\n";
    // LAB 2-9 : 비트 연산 해보기
    // 변수 num_2s에 64를 저장합니다. 
    // num_2s >> 1, num_2s>>6, num_2s>>10, num_2s <<1, num_2s<<6, num_2s<<10을 출력합니다.
    int num_2s = 64;
    std::cout << (num_2s >> 1) << " " << (num_2s >> 6) << " " << (num_2s >> 10) << " "
        << (num_2s << 24) << " " << (num_2s << 25) << " " << (num_2s << 26) << std::endl; // C++ 출력
    printf("%d %d %d %d %d %d\n", num_2s >> 1, num_2s >> 6, num_2s >> 10, num_2s << 24, num_2s << 25, num_2s << 26); // C 출력

    std::cout << "\nLAB 2-10\n";
    // LAB 2-10 : 키보드 입력
    // 변수 input_str에 키보드 입력을 받아서 저장하고, 앞에 " input string: "를 붙여서 출력합니다. 
    std::string input_str;
    std::cin >> input_str;
    std::cout << " input string: " << input_str << std::endl; // C++

    char input_str2[100];
    scanf_s("%99s", input_str2, 100);
    printf(" input string: %s\n", input_str2);


    // 심화학습 : 파이썬 input 함수를 C++로 구현해보기
    auto input = [](const char* msg) {
        std::cout << msg;
        std::string input_str;
        std::cin >> input_str;
        return input_str;
    };

    std::cout << input("Test input: ") << " ...ok" << std::endl; // 테스트

    // 심화학습 : 파이썬 print 함수를 C++로 구현해보기

    std::string sep = " ";
    std::string end = "\n";

    auto print = [sep, end](auto... inputs) {        
        int _[] = { (std::cout << inputs << sep, 0)... };
        std::cout << end;
    };

    print("Test print:", 1, 'g', 0.0, true, "...ok"); // 테스트
}
