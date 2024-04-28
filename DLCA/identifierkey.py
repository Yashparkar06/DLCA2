import re

keywords = {
    r'if': 'Keyword (if)', r'else': 'Keyword (else)', r'while': 'Keyword (while)',
    r'for': 'Keyword (for)', r'break': 'Keyword (break)', r'continue': 'Keyword (continue)',
    r'return': 'Keyword (return)', r'int': 'Keyword (int)', r'float': 'Keyword (float)',
    r'char': 'Keyword (char)', r'double': 'Keyword (double)', r'void': 'Keyword (void)'
}

input_str = input("Enter the expression: ")
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'

identifiers = re.findall(identifier_pattern, input_str)
for identifier in identifiers:
    print("Identifier:", identifier)

for keyword, description in keywords.items():
    if re.search(r'\b' + keyword + r'\b', input_str):
        print(description)


# ouput:
# Enter the expression:   if x > 0:
# Identifier: if
# Identifier: x
# Keyword (if)