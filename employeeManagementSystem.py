class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getID(self):
        return self.id
    
    def getDepartment(self):
        return self.department

    def __str__(self):
        return f"Employee id: {self.getID()}\nName: {self.getName()}\nAge: {self.getAge()}\nDepartment: {self.getDepartment()}"

class EmployeeManagementSystem:
    def __init__(self):
        self.employeeList = []
    
    def addEmployees(self, id, name, age, department):
        if not id.isdigit():
            raise ValueError("ID must be a valid integer")
        if int(id) <= 0:
            raise ValueError("ID must be a positive integer greater than 0")
        
        for i in self.employeeList:
            if int(id) == i.getID():
                raise ValueError("ID already exists")

        if not name.isalpha():
            raise ValueError("Invalid name")
        if not age.isdigit():
            raise ValueError("Age must be a valid integer")
        if not (18 <= int(age) < 70):
            raise ValueError("Age must be between 18 and 70")
        if department.lower().strip() not in ["training and development", "human resources", "public relations", "marketing", "finance", "it"]: 
            raise ValueError("Invalid department")
        self.employeeList.append(Employee(name.strip(), int(age), int(id), department.strip().upper()))

    def getEmployeeInfo(self, id):
        if not id.isdigit():
            raise ValueError("invalid ID")
        for i in self.employeeList:
            if int(id) == i.getID():
                return i
        raise ValueError(f"Employee with ID: {id} does not exist")
            
    def deleteEmployee(self, id):
        if not id.isdigit():
            raise ValueError("invalid ID")
        for i in self.employeeList:
            if int(id) == i.getID():
                self.employeeList.remove(i)
                return
        raise ValueError(f"Employee with ID: {id} does not exist")
    
def main():
    company1 = EmployeeManagementSystem()
    while True:
        try:
            print("\nChoose one of the following options:")
            choice = input("\n\t1. Add new employee\n\t2. Get employee info\n\t3. Delete employee\n\tType 'q' to quit\n\nEnter your choice: ").strip()

            if choice == "1":
                id = input("\nEnter employee ID: ")
                name = input("Enter employee name: ")
                age = input("Enter employee age: ")
                department = input("Enter employee department (Training and Development, Human Resources, Public Relations, Marketing, Finance, IT): ")
                company1.addEmployees(id, name, age, department)

            elif choice == "2":
                id = input("\nEnter employee id: ")
                print(company1.getEmployeeInfo(id))
                print()

            elif choice == "3":
                id = input("\nEnter employee id: ")
                company1.deleteEmployee(id)
                print("Employee deleted successfully")

            elif choice == "q":
                break

            else:
                print("Please enter valid input")

        except ValueError as e:
            print()
            print(e)
            print("Please try again.")
        except Exception as e:
            print("\nAn unexpected error occurred:", e)
            print("Please try again.")

if __name__ == '__main__':
    main()
