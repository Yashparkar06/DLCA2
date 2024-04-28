class CodeGenerator:
    def __init__(self):
        self.next_temp = 0

    def generate_temp(self):
        temp = f"t{self.next_temp}"
        self.next_temp += 1
        return temp

    def generate_code(self, node):
        if node.type == 'number':
            return f"MOV {node.value}, {node.result}"
        elif node.type == 'binary_op':
            left_code = self.generate_code(node.left)
            right_code = self.generate_code(node.right)
            temp = self.generate_temp()
            op = self.get_operator(node.value)
            code = f"{left_code}\n{right_code}\n{op} {node.left.result}, {node.right.result}, {temp}"
            return code
        else:
            raise ValueError(f"Invalid node type: {node.type}")

    def get_operator(self, operator):
        if operator == '+':
            return "ADD"
        elif operator == '-':
            return "SUB"
        elif operator == '*':
            return "MUL"
        elif operator == '/':
            return "DIV"
        else:
            raise ValueError(f"Invalid operator: {operator}")

class Node:
    def __init__(self, type, value=None, left=None, right=None, result=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right
        self.result = result

# Function to parse the input expression into an AST
def parse_expression(expression):
    # Your parsing logic goes here
    # For simplicity, we'll create a simple AST directly
    ast = Node('binary_op', '+',
               Node('number', 3),
               Node('binary_op', '*',
                    Node('number', 4),
                    Node('number', 5)))
    return ast

# Get input from the user
expression_str = input("Enter an arithmetic expression: ")

# Parse the input expression into an AST
ast = parse_expression(expression_str)

# Generate code
generator = CodeGenerator()
code = generator.generate_code(ast)

# Print the generated code
print("Generated Code:")
print(code)

# ouput:
# Enter an arithmetic expression:  3 * (4 + 5)
# Generated Code:
# MOV 3, None
# MOV 4, None
# MOV 5, None
# MUL None, None, t0
# ADD None, None, t1