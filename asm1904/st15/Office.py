from .Department import Department
from .Employee import Employee
from .functions import *
import pickle


class Office:
    dbase=[]

    def Add_Department(self):
        department = Department()
        department.AddDepartment()
        self.dbase.append(department)

    def Add_Employee(self):
        employee = Employee()
        employee.Add_Employee()
        self.dbase.append(employee)

    def ShowDB(self):
        print("\nThe present DataBase of office: \n")
        for i in self.dbase:
            print("\n(ID:" + str(self.dbase.index(i)) + ")")
            i.Show()

    def SaveDB(self):

        file = input("FileName to save to\n")
        with open(str(file)+".dat", "wb")as f:
            pickle.dump(self.dbase, f)
        print("File saved")


    def loadDB(self):
        while (True):
            filename = input('Enter file name\n')
            if (is_file(filename)):
                with open(str(filename)+".dat", 'rb') as f:
                    print(f)
                    self.dbase = pickle.load(f)
                    print("Success!!!")
                    self.ShowDB()
                break
            else:
                print('Error reading the file')
                break


    def ClearDB(self):
        self.dbase.clear()
        print("DataBase successfully cleared!")

    def EditDB(self):
        while (True):

            if (len(self.dbase) > 0):
                self.ShowDB()
                buf = int(input("Choose Data ID from DataBase\n"))
                if buf < len(self.dbase):
                    self.dbase[buf].EditDep()
                    break
                else:
                    repeat = input("Data doesn't exist.Repeat? Y/N\n")
                    if (str.lower(repeat) != 'y'):
                        break
            else:
                print("Database is empty")
                break




