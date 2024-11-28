class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class PermanentEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


permanent = PermanentEmployee("Fahim", 101, 5000)
contract = ContractEmployee("Sakib", 102, 20, 120)

print(f"{permanent.name}'s Salary: {permanent.calculate_salary()}")
print(f"{contract.name}'s Salary: {contract.calculate_salary()}")