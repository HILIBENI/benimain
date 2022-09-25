letterlist = []
wordlist = []

#take input, create list of characters
def letterize(input):
    for i in input:
        if i != " ":
            letterlist.append(i)





    



occurence = {}


if __name__ == "__main__":
    sentence = input("adjon meg egy mondatot: ") 
    letterize(sentence)

    for i in letterlist:
        if i not in occurence: #check if letter is in the dict, if not - create a new entry
            occurence[i] = 1
        elif i in occurence: #check if letter is in the dict, if yes - update dict value to be +1
            value = occurence.get(i)
            occurence.update({i : value + 1})
    
    wordlist = sentence.split(" ")
    wordlist.sort()

    


print("Betűk gyakorisága:", occurence)


print("Fordítva:", letterlist[::-1]) # same as letterlist.reverse(), but more elegant


print("Listába rendezve szavanként:", wordlist)

        
