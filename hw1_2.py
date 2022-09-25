

def convert(x, unit):

    if unit == "cm":
        cm = float(x) * 0.39
        print(round(cm, 2), "inches") 
    elif unit == "inch":
        inch = float(x) * 2.54
        print(round(inch, 2), "cm") 
    elif unit != "cm" or "inch":
        print("Not correct unit!")    



    





if __name__ == "__main__":
    num = input("Adjon meg egy számot és egy mértékegységet (cm/inch): ")
    separatedstr = num.split(" ")
    number = separatedstr[0]
    unit = separatedstr[1]
    convert(number, unit)

    