
if __name__ == "__main__":
    while True:
        a = int(input("Enter 'a' value: "))
        b = int(input("Enter 'b' value: "))
        try:
            z = a / b
            print(z)
        except ZeroDivisionError:
            print("Division by zero not allowed")
            break
        finally:
            print("Out of try except block")
