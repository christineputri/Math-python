command = ""

while input != "exit":
    print("Welcome to Mini Calculator")
    print("Option\t:")
    print("- plus")
    print("- minus")
    print("- times")
    print("- divide")
    print("- modulo")
    print("- exit")
    
    if command == "exit":
        break
    command = input("Input: ")
    if command != "plus" and command != "minus" and command != "times" and command != "divide" and command != "modulo":
        print("Please re-input!\n")
        continue

    a = int(input("Input first number\t: "))
    b = int(input("Input second number\t: "))

    if command == "plus":
        result = a+b
    elif command == "minus":
        result = a-b
    elif command == "times":
        result = a*b
    elif command == "divide":
        result = a/b
    elif command == "modulo":
        result = a%b
    
    print(f"Hasil\t\t\t: {result}\n")
    
print ("Thankyou\n")