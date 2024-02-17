import unittest
from employeeManagementSystem import EmployeeManagementSystem

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.employee_system = EmployeeManagementSystem()

    def test_addEmployees(self):
        # Test adding a valid employee
        self.employee_system.addEmployees("1", "Mazin", "25", "Training and Development")
        self.assertEqual(len(self.employee_system.employeeList), 1)

        # Test for invalid ID
        with self.assertRaises(ValueError):
            self.employee_system.addEmployees("a", "Mazin", "30", "IT")

        # Test for invalid age
        with self.assertRaises(ValueError):
            self.employee_system.addEmployees("2", "Mazin", "xyz", "IT")

        # Test for invalid name
        with self.assertRaises(ValueError):
            self.employee_system.addEmployees("2", "", "30", "IT")

        # Test for invalid department
        with self.assertRaises(ValueError):
            self.employee_system.addEmployees("2", "Mazin", "30", "Sales")

    def test_getEmployeeInfo(self):
        self.employee_system.addEmployees("2", "Ahmed", "25", "Training and Development")
        self.employee_system.addEmployees("3", "Ekram", "30", "Marketing")

        # Test for getting an employee info
        employee_info = self.employee_system.getEmployeeInfo("2")
        self.assertEqual(employee_info.getName(), "Ahmed")
        self.assertEqual(employee_info.getAge(), 25)
        self.assertEqual(employee_info.getDepartment(), "TRAINING AND DEVELOPMENT")

        # Test for getting a non-existing employee
        with self.assertRaises(ValueError):
            self.employee_system.getEmployeeInfo("100")

    def test_deleteEmployee(self):
        # Add some employees for testing
        self.employee_system.addEmployees("2", "Ahmed", "25", "Training and Development")
        self.employee_system.addEmployees("3", "Ekram", "30", "Marketing")

        # Test deleting an existing employee
        self.employee_system.deleteEmployee("2")
        self.assertEqual(len(self.employee_system.employeeList), 1)

        # Test for deleting a non-existing employee
        with self.assertRaises(ValueError):
            self.employee_system.deleteEmployee("100")

if __name__ == '__main__':
    unittest.main()
