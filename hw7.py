def szoveg():
    t = open('hazi.txt', 'r',encoding='utf8')
    for i in t:
        if i != '\n':
            linelist.append(i.rstrip('\n'))
    




linelist = []

if __name__ == "__main__":
    szoveg()