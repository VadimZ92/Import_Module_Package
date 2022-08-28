def get_employees():
    db1 = {}
    key = 1
    while key == 1:
        name = input("Введите имя рабочего:\n")
        salary = int(input(f"Введите зарплату, которую получает {name}:\n"))
        db = {name: salary}
        db1.update(db)
        exit_ = input("Продолжить?:\n")
        if exit_ == "да":
            key = 1
        else:
            key = 0
    return print(db1)
