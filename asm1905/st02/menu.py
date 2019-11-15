if __name__ == '__main__':
    from cottages import cottage
else:
    from .cottages import cottage



    
def menu(MENU, cottage1):
    print("------------------------------")
    print("You are welcome in "+cottage1.name)
    for i, item in enumerate(MENU):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())

def startMenu():
    try:
        cottage1 = cottage()
        MENU = [
            ['Add house', cottage1.addHouse],
            ['Output house(s)', cottage1.outputHouse],
            ['Change house', cottage1.changeHouse],
            ['Read cottage from file', cottage1.readFromFile],
            ['Write cottage to file', cottage1.writeToFile],
            ['Clear cottage', cottage1.clearCottage]
        ]
        while True:
            MENU[menu(MENU, cottage1)][1]()
    except Exception as ex:
        print(ex, "\nbye")