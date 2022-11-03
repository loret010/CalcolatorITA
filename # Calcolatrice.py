# Calcolatrice


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Seleziona operazione.")
print("1.Addizione")
print("2.Sottrazione")
print("3.Moltiplicatore")
print("4.Divisione")

while True:
    
    choice = input("Inserire i numeri corrispondenti all'operazione: ")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Inserisci primo numero: "))
        num2 = float(input("Inserisci secondo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        
        next_calculation = input("Vuoi fare un'altro calcolo? (Scrivere yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")