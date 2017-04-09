from List import LiuDataStructure, List
from Stack import Stack
from Queue import Queue

class ShuntingYard(LiuDataStructure):
    # Test if a certain token is operator
    @staticmethod
    def __is_operator__(token):
        return token in ShuntingYard.OPERATORS.keys()

    # Test the associativity type of a certain token
    @staticmethod
    def __is_assoc_type__(token, assoc):
        if not ShuntingYard.__is_operator__(token):
            raise ValueError('Invalid token: %s' % token)
        return ShuntingYard.OPERATORS[token][1] == assoc

    # Compare the precedence of two tokens
    @staticmethod
    def __cmp_precedence__(token1, token2):
        if not ShuntingYard.__is_operator__(token1) or not ShuntingYard.__is_operator__(token2):
            raise ValueError('Invalid tokens: %s %s' % (token1, token2))
        return ShuntingYard.OPERATORS[token1][0] - ShuntingYard.OPERATORS[token2][0]

    # Transforms an infix expression to RPN
    @staticmethod
    def digest(tokens):
        out = Queue()
        stack = Stack()
        # For all the input tokens [S1] read the next token [S2]
        for token in tokens:
            if ShuntingYard.__is_operator__(token):
                # If token is an operator (x) [S3]
                while not stack.is_empty() and ShuntingYard.__is_operator__(stack.peek()):
                    # [S4]
                    if (ShuntingYard.__is_assoc_type__(token, ShuntingYard.LEFT_ASSOC) \
                                and ShuntingYard.__cmp_precedence__(token, stack.peek()) <= 0) or \
                            (ShuntingYard.__is_assoc_type__(token, ShuntingYard.RIGHT_ASSOC) \
                                     and ShuntingYard.__cmp_precedence__(token, stack.peek()) < 0):
                        # [S5] [S6]
                        out.enqueue(stack.pop())
                        continue
                    break
                # [S7]
                stack.push(token)
            elif token == '(':
                stack.push(token)  # [S8]
            elif token == ')':
                # [S9]
                while not stack.is_empty() and stack.peek() != '(':
                    out.enqueue(stack.pop())  # [S10]
                stack.pop()  # [S11]
            else:
                out.enqueue(token)  # [S12]
        while not stack.is_empty():
            # [S13]
            out.enqueue(stack.pop())
        return out

    @staticmethod
    def calculate(tokens):
        ''' Evaluate RPN expr (given as string of tokens) '''
        stack = Stack()
        for token in tokens:
            if token in ShuntingYard.OPERATORS.keys():
                stack.push(ShuntingYard.OPERATORS[token][2](stack.pop(), stack.pop()))
            else:
                stack.push(float(token))
        return stack.pop()


ShuntingYard.LEFT_ASSOC = 0
ShuntingYard.RIGHT_ASSOC = 1
ShuntingYard.OPERATORS = {
    '+': (0, ShuntingYard.LEFT_ASSOC, (lambda x, y: x + y)),
    '-': (0, ShuntingYard.LEFT_ASSOC, (lambda x, y: y - x)),
    '*': (5, ShuntingYard.LEFT_ASSOC, (lambda x, y: y * x)),
    '/': (5, ShuntingYard.LEFT_ASSOC, (lambda x, y: y / x)),
    '%': (5, ShuntingYard.LEFT_ASSOC, (lambda x, y: y % x)),
    '^': (10, ShuntingYard.RIGHT_ASSOC, (lambda x, y: y ** x))
}

if __name__ == '__main__':
    input = "1*2+5"
    output = ShuntingYard.digest(input)
    print(output)
    print(ShuntingYard.calculate(output))
    print(1*2+5)

    input = "(1+2)*(3/4)^(5+6)"
    output = ShuntingYard.digest(input)
    print(output)
    print(ShuntingYard.calculate(output))
    print((1 + 2) * (3 / 4) ** (5 + 6))

    input = "1+2*3/4^5+6"
    output = ShuntingYard.digest(input)
    print(output)
    print(ShuntingYard.calculate(output))
    print(1 + 2 * 3 / 4 ** 5 + 6)

    input = "1*2/3%9-4^5+6"
    output = ShuntingYard.digest(input)
    print(output)
    print(ShuntingYard.calculate(output))
    print(1*2/3%9-4**5+6)
