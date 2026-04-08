import math

def scientific_calculator():
    print("=== Scientific Calculator ===")
    print("Available operations: add, sub, mul, div, sin, cos, tan, log, exp, sqrt, factorial")
    
    while True:
        op = input("\nEnter operation (or 'exit' to quit): ").lower()
        if op == "exit":
            print("Exiting calculator...")
            break
        
        if op in ["add", "sub", "mul", "div"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == "add":
                print("Result:", a + b)
            elif op == "sub":
                print("Result:", a - b)
            elif op == "mul":
                print("Result:", a * b)
            elif op == "div":
                print("Result:", a / b if b != 0 else "Error: Division by zero")
        
        elif op in ["sin", "cos", "tan", "log", "exp", "sqrt", "factorial"]:
            x = float(input("Enter number: "))
            if op == "sin":
                print("Result:", math.sin(math.radians(x)))
            elif op == "cos":
                print("Result:", math.cos(math.radians(x)))
            elif op == "tan":
                print("Result:", math.tan(math.radians(x)))
            elif op == "log":
                print("Result:", math.log(x))
            elif op == "exp":
                print("Result:", math.exp(x))
            elif op == "sqrt":
                print("Result:", math.sqrt(x))
            elif op == "factorial":
                print("Result:", math.factorial(int(x)))
        else:
            print("Invalid operation. Try again.")

if __name__ == "__main__":
    scientific_calculator()
