# %% [markdown] lang="en" tags=["slide"]
#
# ## Workshop: Employees
#
# In the following we will implement a class hierarchy for employees of a company:
#
# - Employees can be either workers or managers
# - Each employee of the company has a name, a personnel number and a
#   base salary
# - For each worker, the accumulated overtime and the hourly wage
#   are stored in attributes.
# - A worker's salary is calculated as 13/12 times the
#   base salary plus overtime pay
# - Each manager has an individual bonus
# - A manager's salary is calculated as 13/12 times the
#   base salary plus bonus
#
# Implement Python classes `Employee`, `Worker` and `Manager` with
# appropriate attributes and a method `salary()` that calculates the salary.


# %% tags=["alt"]
class Employee:
    def __init__(self, name, pers_nr, base_salary):
        self.name = name
        self.pers_nr = pers_nr
        self.base_salary = base_salary

    def salary(self):
        return 13 / 12 * self.base_salary


# %% tags=["alt"]
class Worker(Employee):
    def __init__(self, name, pers_nr, base_salary, overtime, hourly_wage):
        super().__init__(name, pers_nr, base_salary)
        self.overtime = overtime
        self.hourly_wage = hourly_wage

    def __repr__(self):
        return (
            f"Worker({self.name!r}, {self.pers_nr!r}, {self.base_salary}, "
            f"{self.overtime}, {self.hourly_wage})"
        )

    def salary(self):
        return super().salary() + self.overtime * self.hourly_wage


# %% tags=["alt"]
class Manager(Employee):
    def __init__(self, name, pers_nr, base_salary, bonus):
        super().__init__(name, pers_nr, base_salary)
        self.bonus = bonus

    def __repr__(self):
        return (
            f"Manager({self.name!r}, {self.pers_nr!r}, {self.base_salary}, "
            f"{self.bonus})"
        )

    def salary(self):
        return super().salary() + self.bonus


# %% tags=["alt"]
a = Worker("Hans", 123, 36_000, 3.5, 40)

# %%
assert a.salary() == 39_140.0

# %% tags=["alt"]
m = Manager("Sepp", 834, 60_000, 30_000)

# %%
assert m.salary() == 95_000.0
