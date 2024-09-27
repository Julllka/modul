from application.people import get_employees as get_employees
from application.salary import calculate_salary as calculate_salary
from datetime import datetime

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now())