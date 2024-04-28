class IntermediateCodeGenerator:
    def __init__(self):
        self.next_temp = 0

    def generate_temp(self):
        temp = f"t{self.next_temp}"
        self.next_temp += 1
        return temp

    def generate_code(self, expression):
        if len(expression) == 1:  # If expression is a single variable or constant
            return expression
        
        op = expression[1]
        if op in {'+', '-', '*', '/'}:  # If expression is a binary operation
            temp1 = self.generate_code(expression[0])
            temp2 = self.generate_code(expression[2])
            temp = self.generate_temp()
            print(f"{temp1} {op} {temp2} = {temp}")
            return temp
        else:
            return expression[0]  # If expression is a single variable or constant

# Example usage:
generator = IntermediateCodeGenerator()
expression = ['x', '+', ['y', '*', 'z']]
result = generator.generate_code(expression)
print("Result:", result)
