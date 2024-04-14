# ask user for first n
# ask user for second n
# have user choose an operation to perform
# perform operation on two ns
# print result to terminal
def prompt(message):
    print(f"===> {message}")

prompt("Welcome to calc")
input()
prompt("Enter first number: ")
n1 = int(input())
prompt("Enter second number: ")
n2 = int(input())
prompt("Which operation? (+ - x /): ")
operation = input()

match operation:
    case "+":
        ans =  n1 + n2
    case "-":
        ans = n1 - n2
    case "x":
        ans = n1 * n2
    case "/":
        ans = n1 / n2

prompt(f"The result is: {ans}") 