def is_palindrome(number):
    split_number = list(str(number))
    number_lenght = int(len(split_number))
    bool=True
    # Even
    if number%2==0:
        for i in range(1, number_lenght,1):
            bool *= split_number[i-1]==split_number[-i]
                    
    # Odd
    else:
        for i in range(1, number_lenght-1,1):
            bool *= split_number[i-1]==split_number[-i]
    
    return bool

print(is_palindrome(1234))
print(is_palindrome(1221))
print(is_palindrome(12021))
print(is_palindrome(120231))

number_max = int("9"*2)
mult_list = list(reversed(range(number_max-10,number_max+1,1)))
print(mult_list)
