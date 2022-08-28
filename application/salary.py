def calculate_salary():
    salary_m = float(input("Введите зарплату за месяц:\n"))
    print("Зарплата за год без вычета налога:", 12 * salary_m)
    print("Зарплата за год после вычета налога:", (12 * salary_m) - (12 * 0.13 * salary_m))
