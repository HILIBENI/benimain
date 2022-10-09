class Developer:
        def __init__(self, name, project, role):
            self.name = name
            self.project = project
            self.role = role

        




if __name__ == "__main__":

    # adding the devs
    dev1 = Developer("Ricsi", "SolArch", "Frontend") 
    dev2 = Developer("Angéla", "ZerTeng", "Tester")
    dev3 = Developer("Peti", "KefERP", "Backend")
    dev4 = Developer("Éva", "KefERP", "Frontend")

    devlist = [dev1, dev2, dev3, dev4]
    person_a = ""
    person_b = ""

    for i in devlist:
        print("--Developer added:--")
        print(i.name, "a", i.project + "-en dolgozik", i.role, "szerepkörben")

    for i in range(len(devlist)): # iterate through every object in the list, comparing them to every object (this is a very bad solution, but it works for now.)
        for x in range(len(devlist)):
            if (devlist[i].project == devlist[x].project) and (devlist[i].name != devlist[x].name): #x.name != i.name > so we dont compare the same person to themselves
                if person_a != devlist[x].name: # remove dupes from the system by comparing them to eachother, only works if there's only one pair. this code is a mess.
                    person_a = devlist[i].name
                    person_b = devlist[x].name
                    print(person_a, "és", person_b, "dolgoznak egy projekten")

        

