import re

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def lex(pattern):
    tokens = []
    number_pattern = r'[0-9]+'
    for match in re.finditer(number_pattern, pattern):
        no = match.group()
        if is_prime(int(no)):
            tokens.append(('PRIME', no))
    
    return tokens

ip = input("Enter numbers separated by spaces: ")
op = lex(ip)
print(op)

# output:
# Enter numbers separated by spaces:   12 27 45 46 69 42 7 4
# [('PRIME', '7')]