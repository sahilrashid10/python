def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1, n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2
#referencing functions
operations = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}
def calculator():
    num1 = int(input("\nEnter 1st no: "))
    flag = True
    while flag:
        for symbols in operations:
            print(symbols)
        to_do = input(f"\nchoose an operation: ")
        num2 = int(input("\nEnter next no: "))
        answer = operations[to_do](num1,num2)
        print(f"Solution = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
           num1 = answer
        else:
            flag = False
            print("\n" * 20)
            calculator()

calculator()

