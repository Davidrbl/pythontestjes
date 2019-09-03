dict = {"David": "1", "Karsten": "2", "Douwe": "3"}
'''dict = open("dict.txt", "w")'''

def delItemCheck(ding):
    delitem = input("Welk item wilt u verwijderen? ")
    del dict[delitem]

def addItem():
    newkey = input("Key: ")
    newvalue = input("Value: ")

    dict[newkey] = newvalue

def viewAll():
    for key, value in dict.items():
        print(key, value)

while True:
    ding = input("Kies tussen de volgende opties:\n \nTyp de naam van uw key:\nZeg add om een item toe te voegen:\nTyp del om een item te verwijderen:\nTyp all om de hele dictionary te zien:\n")
    if ding == "quit":
        break
    elif ding == "add":
        addItem()
    elif ding == "del":
        delItemCheck(ding)
    elif ding == "all":
        viewAll()
    else:
        print(dict[ding])
