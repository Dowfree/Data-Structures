from Stack import Stack
from List import List

def fibonacci_recur(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

def fibonacci_stack(n):
    stack = Stack([n])

    result = 0
    while not stack.is_empty():
        stack.print()
        x = stack.pop()
        if x > 2:
            stack.push(x - 2)
            stack.push(x - 1)
        elif x==1:
            result += 1
        elif x==2:
            result += 2

    return result

def fibonacci_dp(n):

    l = List(max_length=n)
    l.append(1)
    l.append(2)

    for i in range(2,n):
        l.append( l.get(i-1)+l.get(i-2))

    return l.get(n-1)


if __name__ == '__main__':
    #print(fibonacci_recur(20))
    print(fibonacci_stack(20))
    print(fibonacci_dp(20))