import random
import math
import os
afsluiten = False
clear = lambda: os.system('cls')
schermbreedte = 70
dictio = {}

def printAfscheid(schermbreedte):
    printHeader(schermbreedte)
    printRegel("Tot de volgende keer!")
    printFooter(schermbreedte)

def printRegel(regel):
    print(("| {:" + str(schermbreedte - 4)+ "} |").format(regel))

def printHeader(schermbreedte):
    print("_"*schermbreedte)
    print("| " + " "*int(schermbreedte - 4) + " |")

def printFooter(schermbreedte):
    print("| " + " "*int(schermbreedte - 4) + " |")
    print("|_" + "_"* int(schermbreedte - 4) + "_|")

def readFile(source):
    with open(source, "w+") as f:
        text = f.read().split("\n")
        dictio = {}
        for item in text:
            if not item == '':
                key, value = item.split("=")
                dictio[key] = value
        return dictio

def kiesFile():
    printHeader(schermbreedte)
    printRegel("Voer de location van het txt file in.")
    printFooter(schermbreedte)
    fileSource = input()
    readFile(fileSource)
    clear()

def nieuweFile():
    printHeader(schermbreedte)
    printRegel("Voer de locatie die u wilt in voor uw file met de naam van uw file.")
    printFooter(schermbreedte)
    newFileSource = input()
    readFile(newFileSource)
    clear()

def delItemCheck(ding):
    printHeader(schermbreedte)
    printRegel("Welk item uit de lijst wilt u verwijderen?")
    printFooter(schermbreedte)
    delitem = input()
    del dictio[delitem]
    clear()


def addItem():
    printHeader(schermbreedte)
    printRegel("Voer in welke key en value het nieuwe item moet hebben.")
    printFooter(schermbreedte)
    newkey = input("Key: ")
    newvalue = input("Value: ")
    dictio[newkey] = newvalue
    clear()


def viewAll(dictio):
    for key, value in dictio.items():
        printHeader(schermbreedte)
        printRegel(key + "   " + value)
        printFooter(schermbreedte)
    input()
    clear()

def saveToFile(dictio):
    print(dictio)
    printHeader(schermbreedte)
    printRegel("Waar naar welk file moet het worden gesaved?")
    printFooter(schermbreedte)
    saveLocation = input()
    with open(saveLocation, "w") as f:
        for item in dictio:
            f.write(item+"="+dictio[item]+'\n')
    f.close()
    clear()


def quiz(dictio):
    wildoorgaan = True
    allKeys = []
    allValues = []

    for key, value in dictio.items():
        allKeys.append(key)
        allValues.append(value)

    while wildoorgaan == True:
        keyNum = math.floor(random.randint(0, (len(allKeys)-1)))
        quizKey = allKeys[keyNum]
        quizValue = allValues[keyNum]
        printHeader(schermbreedte)
        printRegel("Wat is de value van:     " + quizKey)
        printFooter(schermbreedte)
        answer = input()
        clear()
        printHeader(schermbreedte)
        if answer == quizValue:
            printRegel("Goed gedaan!")
        else:
            printRegel("Helaas, dat is niet het goede antwoord, het goede antwoord is: \t" + quizValue)
        printRegel("Wil je doorgaan? Ja of Nee?")
        printFooter(schermbreedte)
        doorgaanAnswer = input()
        clear()
        if doorgaanAnswer == "Nee":
            wildoorgaan = False




while afsluiten == False:
    print(dictio)
    printHeader(schermbreedte)
    printRegel("Kies tussen de volgende opties.")
    printRegel("Typ 'n' om een nieuwe lijst aan te maken")
    printRegel("Typ 'k' om een andere lijst te kiezen")
    printRegel("Typ 'v' om de huidige lijst te laten zien")
    printRegel("Typ 't' om een item toe te voegen aan een de lijst")
    printRegel("Typ 'd' om een item te verwijderen uit de lijst")
    printRegel("Typ 'o' om je te laten overhoren")
    printRegel("Typ 'w' om de lijst op te slaan")
    printRegel("Typ 'q' om te stoppen")
    printFooter(schermbreedte)
    inpoet = input()
    clear()
    if inpoet == "n":
        nieuweFile()
    elif inpoet == "k":
        kiesFile()
    elif inpoet == "v":
        viewAll(dictio)
    elif inpoet == "t":
        addItem()
    elif inpoet == "d":
        delItemCheck(inpoet)
    elif inpoet == "o":
        quiz(dictio)
    elif inpoet == "w":
        saveToFile(dictio)
    elif inpoet == "q":
        afsluiten = True
        printAfscheid(schermbreedte)
