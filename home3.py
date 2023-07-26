from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()

    current_weekday = today.weekday()

    birthdays_by_weekday = {i: [] for i in range(7)}

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        days_until_birthday = (birthday - today).days

        birthday_weekday = (current_weekday + days_until_birthday) % 7

        birthdays_by_weekday[birthday_weekday].append(name)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for weekday_index, birthday_names in birthdays_by_weekday.items():
        if birthday_names:
            weekday_name = weekdays[weekday_index]
            print(f"{weekday_name}: {', '.join(birthday_names)}")

users = [
    {'name': 'Dmytro', 'birthday': datetime(2023, 7, 27)},
    {'name': 'Alex', 'birthday': datetime(2023, 7, 29)},
    {'name': 'Iryna', 'birthday': datetime(2023, 7, 31)},
    {'name': 'Oleg', 'birthday': datetime(2023, 8, 1)},
]

get_birthdays_per_week(users)
