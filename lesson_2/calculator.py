# ask user for first n
# ask user for second n
# have user choose an operation to perform
# perform operation on two ns
# print result to terminal
def prompt(message):
    print(f"===> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

prompt("Welcome to calc")
input()
prompt("Enter first number: ")
n1 = input()

while invalid_number(n1):
    prompt("Invalid number")
    n1 = input()

prompt("Enter second number: ")
n2 = input()

while invalid_number(n2):
    prompt("Invalid number")
    n2 = input()

prompt("Which operation? (+ - x /): ")
operation = input()

while operation not in ["+", "-", "x", "/"]:
    prompt("You must choose + - x or /")
    operation = input()

match operation:
    case "+":
        ans =  int(n1) + int(n2)
    case "-":
        ans = int(n1) - int(n2)
    case "x":
        ans = int(n1) * int(n2)
    case "/":
        ans = int(n1) / int(n2)

prompt(f"The result is: {ans}") 