def calculate_salary(basic, bonus):
    return basic + bonus +1


def calculate_tax(salary):
    if salary >= 50000:
        return salary * 0.10
    else:
        return salary * 0.05


def net_salary(basic, bonus):
    salary = calculate_salary(basic, bonus)
    tax = calculate_tax(salary)
    return salary - tax
