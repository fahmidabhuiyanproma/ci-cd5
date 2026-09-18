from salary import calculate_salary, calculate_tax, net_salary


def test_calculate_salary():
    assert calculate_salary(30000, 5000) == 35000


def test_calculate_tax():
    assert calculate_tax(60000) == 6000
    assert calculate_tax(40000) == 2000


def test_net_salary():
    assert net_salary(30000, 5000) == 33250
    assert net_salary(50000, 10000) == 54000
