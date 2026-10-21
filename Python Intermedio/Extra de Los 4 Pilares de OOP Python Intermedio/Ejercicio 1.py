class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    def promote(self, percentage):
        self.salary = self._salary + self._salary * percentage


def main():
    employee = Employee("Paúl Solano", 120000)
    print(f"Employee Name: {employee.name}")
    print(f"Employee Salary: {employee.salary}")
    employee.promote(0.1)
    print(f"Employee Salary after promotion: {employee.salary}")

    try:
        employee.salary = -500
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()