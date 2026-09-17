# Functions for basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("=== Simple Python Calculator ===")
    
    while True:
        # Display choice menu
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        
        # Check if user wants to exit
        if choice == '5':
            print("Goodbye!")
            break
            
        # Check if choice is one of the valid options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            # Perform the calculation based on the choice
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)  # Prints the division by zero error message
                else:
                    print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input! Please choose a valid option (1-5).")

# Start the calculator program
if __name__ == "__main__":
    calculator()
