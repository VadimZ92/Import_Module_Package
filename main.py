import application.salary
import application.db.people
from datetime import datetime, date, time
from spacex_py import launches

if __name__ == '__main__':
    application.salary.calculate_salary()
    print()
    application.db.people.get_employees()
    print()
    date = date.today()
    print("Текущая дата:", date)
    print()
    print("Первый пилотируемый полёт на/с МКС компании SpaceX:")
    print()
    got_launches, _ = launches.get_launches(payload_id='Crew-1')
    print(got_launches)
