afsluiten = False

def readFile():
    with open(r"C:\Users\david\Desktop\New folder (2)\dict.txt") as f:
        text = f.read().split("\n")

        dictio = {}

        for item in text:
            if not item == '':
                key, value = item.split("=")
                dictio[key] = value
        return dictio


def delItemCheck(ding):
    delitem = input("Welk item wilt u verwijderen? ")
    del dictio[delitem]

def addItem():
    newkey = input("Key: ")
    newvalue = input("Value: ")
    dictio[newkey] = newvalue

def viewAll():
    for key, value in dictio.items():
        print(key + "\t" + value)

def saveToFile(dictio):
    with open(r"C:\Users\david\Desktop\New folder (2)\dict.txt", "w") as f:
        for item in dictio:
            f.write(item+"="+dictio[item]+'\n')

dictio = readFile()


while afsluiten == False:
    ding = input("Kies tussen de volgende opties:\n \nTyp de naam van uw key:\nZeg add om een item toe te voegen:\nTyp del om een item te verwijderen:\nTyp all om de hele dictionary te zien:\nTyp quit om op te slaan en af te sluiten\n")
    if ding == "quit":
        afsluiten = True
        saveToFile(dictio)
    elif ding == "add":
        addItem()
    elif ding == "del":
        delItemCheck(ding)
    elif ding == "all":
        viewAll()
    else:
        print(dictio[ding])
