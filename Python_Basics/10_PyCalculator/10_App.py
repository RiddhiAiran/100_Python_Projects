import logo

def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operations = {'+': add,
              '-': sub,
              '*': multi,
              '/': div
              }
def calculator():
    print(logo.pic)
    num1 = float(input("What's The First Number : "))
    status = True
    while status:
        for symbol in operations:
            print(symbol)

        ope_symbol = input("Pick an Operator : ")
        num2 = float(input("What's The Second Number : "))
        result = operations[ope_symbol](num1,num2)
        print(f"Result : {num1} {ope_symbol} {num2} = {round(result,2)}")

        should_continue = input(f"Type 'y' to continue calculating with {round(result,2)}, or type 'n' to start a new calculation: ").lower()
        if should_continue == 'y':
            num1 = result
        elif should_continue == 'n':
            status = False
            print("\n")
            calculator()
        else:
            break

calculator()
print(add(3,4))