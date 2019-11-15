import pickle
if __name__ == '__main__':
    from stone_houses import stone_house
    from wood_houses import wood_house
else:
    from .stone_houses import stone_house
    from .wood_houses import wood_house
#import os

class cottage():

    def __init__(self):
        self.houses = []
        self.last_file_name = 'cottage.p'
        name = input("Input name of your Cottage: ")
        if (name == ""):
            name = "Some Cottage"
        self.name = name
        
    def addHouse(self):
        print('Cottage \'', self.name, '\'...')
        #str = input("Input number of House to add: ")
        #number = int('-1' if str == '' else str)
        #self.printHouse(number)
        name = input("Input changed name (no input for save curr name): ")
        str = input("Input square of House to change (no input for save curr square): ")
        square = int('0' if str == '' else str)
        num_mat = input('Input material of House (0 - stone, 1 - wood): ')
        
        if (num_mat == '1'):
            print("Wood")
            house = wood_house(name, square)
        elif (num_mat == '0'):
            print("Stone")
            house = stone_house(name, square)
        self.houses.append(house)
        print('House №', len(self.houses), ' is added!')
        
    
    def outputHouse(self):
        print('Cottage \'', self.name, '\'...')
        str = input("Input number of House for print: ")
        number = int('-1' if str == '' else str)
        self.printHouse(number)
        
    def printHouse(self, number):
        if (number == ''):
            number=-1
        if (number == -1):
            for i, house in enumerate(self.houses):
                print('House №', i+1, ' have info:')
                house.outputAllInfo()
                print('\n')
        elif (number > 0) and (number <= len(houses)):
            print('House №', number, ' have info:')
            house = houses[number-1]
            house.outputAllInfo()
            print('\n')
        else:
            print('Not correct number!')
            
    def clearCottage(self):
        self.houses = []
        print('Cottage \'', self.name, '\' is cleared!')
    
    #write cottage to file
    def writeToFile(self):
        file_name = input("Input file name for save: ")
        if (file_name == ""):
            file_name = self.last_file_name
        self.last_file_name = file_name
        with open(file_name, 'wb') as file:
            pickle.dump(self.houses, file)
            print('Cottage is saved to '+file_name+"!")

    #read cottage from file
    def readFromFile(self):
        file_name = input("Input file name for open: ")
        if (file_name == ""):
            file_name = self.last_file_name
        self.last_file_name = file_name
        with open(file_name, 'rb') as file:
            self.houses = pickle.load(file)
            print('Cottage is loaded from '+file_name+"!")
            
    def changeHouse(self):
        print('Cottage \'', self.name, '\'...')
        str = input("Input number of House to change: ")
        number = int('-1' if str == '' else str)
        self.printHouse(number)
        name = input("Input changed name (no input for save curr name): ")
        str = input("Input square of House to change (no input for save curr square): ")
        square = int('0' if str == '' else str)
        #num_mat = input('Input material of House (0 - stone, 1 - wood): ')
        # if (num_mat == '1'):
            # material = material_types.stoneType()
        # elif (num_mat == '0'):
            # material = material_types.woodType()
        
        if (number == -1):
            number = len(self.houses)

        if (number > 0) and (number <= len(self.houses)):
            print('Change house №', number, ':')
            house = self.houses[number-1]
            house.setAllInfo(name, square)
            print('\n')
        else:
            print('Not correct number!')