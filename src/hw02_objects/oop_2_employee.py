"""
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...) (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 points)

c) Draw a UML class diagram for your Employee class. (1 point)
"""


class Employee:
    def __init__(self, age, pID, name, surename, depart, mon_salary, married=False):
        self.age = age
        self.ID = pID
        self.name = name
        self.surename = surename
        self.department = depart
        self.salary = mon_salary
        self.married = married

    def __str__(self):
        res = "*** Arbeitnehmer-Info ***\n"
        res += "Name: " + self.name +" "+ self.surename +"\n"
        res += "Alter: "+ str(self.age) +"\n"
        res += "Personalnummer: " + str(self.ID) +"\n"
        res += "Abteilung: " + self.department + "\n"
        res += "Gehalt: " + str(self.salary) +"\n"
        res += "Verheiratet: " + str(self.married) + "\n\n"
        return res

    def change_marital_status(self, new_surename = None):
        '''Verändert den Status Verheiratet'''
        if not self.married:
            if new_surename != None:
                self.surename = new_surename
            self.married = True
        else:
            if new_surename != None:
                self.surename = new_surename
            self.married = False

    def change_salary(self, amount):
        '''Verändert das Gehalt'''
        self.salary = amount

    def change_department(self, new_department):
        '''Verändert die Abteilung'''
        self.department = new_department





if __name__ == "__main__":
    print("Employee application")

    leo = Employee(29, 1, "Leonhard", "Wabro", "IT-Service", 2500)
    sepp = Employee(25, 2, "Sepp", "Huber", "IT-Service", 2500, True)
    elise = Employee(18, 3, "Elise", "Meyer", "Rezeption", 3000)

    print(leo, sepp, elise)

    elise.change_marital_status("König")
    leo.change_marital_status()

    print(leo, elise)

    sepp.change_department("Rezeption")
    elise.change_salary(4000)

    print(sepp, elise)
