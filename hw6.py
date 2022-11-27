import string

def palindrom():
    for i in word:
        if i not in string.punctuation and i != ' ':
            charlist.append(i)
    if charlist == charlist[::]:
        print('palindrom')
    else:
        print('not palindrom')


charlist = []
if __name__ == "__main__":
    word = "arany nyara"
    palindrom()
    print(charlist[::])