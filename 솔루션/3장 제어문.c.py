# LAB 3-A
# 유저로부터 0 ~ 255 범위의 정수를 입력받습니다.

byte = int(input("Please enter an unsigned 1 byte number: "))

if byte < 0b00000000 or byte > 0b11111111:
    print("out of range")
elif byte <= 0b01111111:
    print("leading byte of a 1-byte utf-8")
elif byte <= 0b10111111:
    print("continuation byte")
elif byte <= 0b11011111:
    print("leading byte of a 2-byte utf-8")
elif byte <= 0b11101111:
    print("leading byte of a 3-byte utf-8")
elif byte <= 0b11110111:
    print("leading byte of a 4-byte utf-8")
else:
    print("not utf-8")

print()

# LAB 3-B
string = input("Please enter a number literal: ")

is_first = True
is_decimal = False
is_after_underscore = False
is_first_zero = False
is_second = False
is_binary = False
is_zero = False
is_error = False
for c in string:
    if is_first:
        is_first = False
        if c > '0' and c <= '9':
            is_decimal = True
            continue
        elif c == '0':
            is_first_zero = True
            is_second = True
            continue
        else:
            is_error = True
            break
    elif is_decimal:
        if not is_after_underscore:
            if c >= '0' and c <= '9':
                continue
            elif c == '_':
                is_after_underscore = True
            else:
                is_error = True
                break
        else:
            if c >= '0' and c <= '9':
                is_after_underscore = False
                continue
            else:
                is_error = True
                break
    elif is_second:
        is_second = False
        if c == '0' or c == '_':
            is_zero = True
            if c=='_':
                is_after_underscore = True
        elif c == 'b' or c == 'B':
            is_binary = True
        else:
            is_error = True
            break
    elif is_zero:
        if is_after_underscore:
            if c == '0':
                is_after_underscore = False
                continue
            else:
                is_error = True
                break
        else:
            if c == '0':
                continue
            elif c == '_':
                is_after_underscore = True
                continue
            else:
                is_error = True
                break
    elif is_binary:
        if is_after_underscore:
            if c == '0' or c == '1':
                is_after_underscore = False
                continue
            else:
                is_error = True
                break
        else:
            if c == '0' or c == '1':
                continue
            elif c == '_':
                is_after_underscore = True
                continue
            else:
                is_error = True
                break

if not is_error:
    if is_decimal or is_zero:
        print("Decimal")
    elif is_binary:
        print("Binary")
    else:
        print("Error")
else:
    print("Error")
            
        
        
        
        








            
