namen = {"David": "1", "Karsten": "2", "Douwe": "3"}


while True:
    ding = input()
    if ding == "quit":
        break
    elif ding == "add":
        newkey = input("Key: ")
        newvalue = input("Value: ")
        namen[newkey] = newvalue
        print(namen)
        input()
    print(namen[ding])
