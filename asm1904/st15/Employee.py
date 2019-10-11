from .Department import Department
from .functions import *
import datetime
now = datetime.datetime.now()
class Employee(Department):
    def __init__(self):
        Department.__init__(self)
        self.FullName = ""
        self.Age = 0
        self.PhoneNum = ""
        self.TurnTo = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
        self.Salary = 0
        self.editlist = {
            "1": ['Organization Name', self.Set_OrgName],
            "2": ['Department Name', self.Set_DepName],
            "3": ['Floor', self.Set_Floor],
            "4": ['Info', self.Set_Info],
            "5": ['Full Name', self.Set_Name],
            "6": ['Age', self.Set_Age],
            "7": ['Extension Phone Number', self.Set_Phone],
            "8": ['Salary', self.Set_Salary],
        }

    def Add_Employee(self):
        Department.AddDepartment(self)
        self.Set_Name()
        self.Set_Age()
        self.Set_Phone()
        self.Set_Salary()

    def Set_Name(self):
        self.FullName = input("Enter full name\n")

    def Set_Age(self):
        self.Age = input("Enter Age\n")
        while (True):
            if is_int(self.Age):
                break
            else:
                self.Age = input("Enter Age\n")

    def Set_Phone(self):
        self.PhoneNum = input("Enter extension number\n")

    def Set_Salary(self):
        self.Salary = input("Enter Salary\n")
        while (True):
            if is_float(self.Salary):
                break
            else:
                self.Salary = input("Enter Salary\n")

    def Show(self):
        Department.Show(self)
        print("\n5. Full Name: "+self.FullName+"\n6. Age: "+self.Age+"\n7. Extension Number: "+self.PhoneNum+"\n8. Turn-to: "+self.TurnTo+"\n9. Salary: "+self.Salary)

    def EditDep(self):
        for i in self.editlist:
            print(i + ' - ' + self.editlist[i][0])
        while (True):
            buf = input("Select a field for editing\n")
            if is_int(buf) and 0 < int(buf) <= len(self.editlist):
                self.editlist[buf][1]()
                break
            else:
                print('Error. This field does not exist')
                answer = input('Change Another Field?\nYes/No')
                if (str.lower(answer) != 'yes'):
                    break