from .functions import*

class Department:
    def __init__(self):
        self.DepName=""
        self.OrganizationName=""
        self.Floor=0
        self.info=""
        self.editlist={
            "1": ['Organization Name', self.Set_OrgName],
            "2": ['Department Name', self.Set_DepName],
            "3": ['Floor', self.Set_Floor],
            "4": ['Info', self.Set_Info],
        }



    def AddDepartment(self):
        self.Set_OrgName()
        self.Set_DepName()
        self.Set_Floor()
        self.Set_Info()

    def Set_DepName(self):
        self.DepName = input ("Enter department name\n")


    def Set_OrgName(self):
        self.OrganizationName = input("Enter organization name\n")

    def Set_Floor(self):
        self.Floor = input("Enter floor\n")
        while (True):
            if is_float(self.Floor):
                break
            else:
                self.Floor = input("Enter floor\n")

    def Set_Info(self):
        self.info = input("Enter additional information\n")

    def Show(self):
        print("\n1. Organization: "+self.OrganizationName+"\n2. Department Name: "+self.DepName+"\n3. Floor: "+self.Floor+"\n4. Info: "+self.info)

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


