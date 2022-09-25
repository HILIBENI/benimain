def szerk(a, b, c):
    if a + b > c:
        if a + c > b:
            if c + b > a:
                print("A", a, b, "és", c, "oldalú háromszög szerkeszthető")
    else:
        print("A", a, b, "és", c, "oldalú háromszög NEM szerkeszthető")
          



if __name__ == "__main__":
    a = int(input("a oldal(cm): "))
    b = int(input("b oldal(cm): "))
    c = int(input("c oldal(cm): "))

    szerk(a, b, c)

        